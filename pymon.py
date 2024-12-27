import atexit
import signal
import sys
from subprocess import Popen
from threading import Timer
from typing import Optional

from rich.console import Console
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

console = Console()
# console.quiet = True


def log_event(message: str, color: str):
    console.log(f"[{color}]{message}[/{color}]")


class PyMon:
    """用于监控 Python 脚本变更并自动重启的工具。"""

    process: Optional[Popen] = None
    restart_timer: Optional[Timer] = None

    def __init__(self, script_path: str):
        self.script_path = script_path
        atexit.register(self.cleanup)

    def start(self):
        if self.process:
            log_event("关闭旧进程...", "yellow")
            self.process.terminate()
            self.process.wait()

        log_event("开启新进程...", "green")
        self.process = Popen(["python", self.script_path])

    def watcher(self, watched_dir: str):
        log_event("初始化文件监视器...", "blue")
        file_event_handler = PatternMatchingEventHandler(patterns=["*.py"])
        setattr(file_event_handler, "on_modified", self.on_file_change_detected)

        file_watcher = Observer()
        file_watcher.schedule(file_event_handler, watched_dir, recursive=True)
        return file_watcher

    def on_file_change_detected(self, event):
        if self.restart_timer:
            self.restart_timer.cancel()

        log_event(f"文件已修改: {event.src_path}", "magenta")
        self.restart_timer = Timer(1, self.start)
        self.restart_timer.start()

    def cleanup(self):
        if self.process:
            log_event("执行清理操作...", "red")
            self.process.terminate()
            self.process.wait()
        if self.restart_timer:
            self.restart_timer.cancel()


def main():
    if len(sys.argv) < 3:
        console.log("[red]用法: python pymon.py <脚本文件路径> <监视目录>[/red]")
        return

    script_path, watched_dir = sys.argv[1], sys.argv[2]

    pymon = PyMon(script_path)
    pymon.start()
    file_watcher = pymon.watcher(watched_dir)

    def handle_exit(signum, frame):
        console.log("[red]收到中断信号，正在退出...[/red]")
        file_watcher.stop()

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    try:
        file_watcher.start()
        console.log("[green]监控文件变更...[/green]")
        while file_watcher.is_alive():
            file_watcher.join(1)
    finally:
        pymon.cleanup()
        console.log("[blue]PyMon 已终止。[blue]")


if __name__ == "__main__":
    main()
