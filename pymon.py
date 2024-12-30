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


def log(msg: str, color: str):
    console.log(f"[{color}]{msg}[/{color}]")


def logsuccess(msg: str):
    log(msg, "green")


def loginfo(msg: str):
    log(msg, "blue")


def logwarn(msg: str):
    log(msg, "yellow")


def logerror(msg: str):
    log(msg, "red")


def logdebug(msg: str):
    log(msg, "magenta")


class PyMon:
    """用于监控 Python 脚本变更并自动重启的工具。"""

    process: Optional[Popen] = None
    restart_timer: Optional[Timer] = None

    def __init__(self, script_path: str):
        self.script_path = script_path

    def start(self):
        if self.process:
            logwarn("关闭旧进程...")
            self.process.terminate()
            self.process.wait()

        loginfo("开启新进程...")
        self.process = Popen(["python", self.script_path])

    def watcher(self, watched_dir: str):
        loginfo("初始化文件监视器...")
        file_event_handler = PatternMatchingEventHandler(patterns=["*.py"])
        setattr(file_event_handler, "on_modified", self.on_file_change_detected)

        file_watcher = Observer()
        file_watcher.schedule(file_event_handler, watched_dir, recursive=True)
        return file_watcher

    def on_file_change_detected(self, event):
        if self.restart_timer:
            self.restart_timer.cancel()

        logdebug(f"文件已修改: {event.src_path}")
        self.restart_timer = Timer(1, self.start)
        self.restart_timer.start()

    def cleanup(self):
        if self.process:
            logwarn("执行清理操作...")
            self.process.terminate()
            self.process.wait()
        if self.restart_timer:
            self.restart_timer.cancel()


def main():
    if len(sys.argv) < 3:
        log("用法: python pymon.py <脚本文件路径> <监视目录>", "red")
        return

    script_path, watched_dir = sys.argv[1], sys.argv[2]

    pymon = PyMon(script_path)
    pymon.start()
    file_watcher = pymon.watcher(watched_dir)

    def handle_exit(signum, frame):
        logerror("收到中断信号，正在退出...")
        file_watcher.stop()

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    try:
        file_watcher.start()
        logsuccess("监控文件变更...")
        while file_watcher.is_alive():
            file_watcher.join(1)
    finally:
        pymon.cleanup()
        logsuccess("PyMon 已终止。")


if __name__ == "__main__":
    main()
