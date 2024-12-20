import sys
from subprocess import Popen
from threading import Timer
from typing import Optional

from rich.console import Console
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

console = Console()


class ScriptReloader:
    process: Optional[Popen] = None
    restart_timer: Optional[Timer] = None
    script_path: str

    def __init__(self, script_path: str):
        self.script_path = script_path

    def start_script(self):
        if self.process:
            self.process.kill()
            print("旧进程已终止。")

        print("启动新脚本进程...")
        self.process = Popen(["python", self.script_path])

    def setup_file_watcher(self):
        print("初始化文件监视器...")
        file_event_handler = PatternMatchingEventHandler(patterns=["*.py"])
        file_event_handler.on_modified = self.on_file_change_detected

        file_watcher = Observer()
        file_watcher.schedule(file_event_handler, "./src/niffler", recursive=True)
        return file_watcher

    def on_file_change_detected(self, event):
        if self.restart_timer:
            self.restart_timer.cancel()

        print(f"检测到文件更改: {event.src_path}")
        self.restart_timer = Timer(1, self.start_script)
        self.restart_timer.start()


def main():
    if len(sys.argv) < 2:
        print("用法: python reloadable.py <脚本文件路径>")
        return

    script_file_path = sys.argv[1]
    reloader = ScriptReloader(script_file_path)
    reloader.start_script()
    file_watcher = reloader.setup_file_watcher()

    try:
        file_watcher.start()
        print("文件监视器已启动。")
        while file_watcher.is_alive():
            file_watcher.join(1)
    except KeyboardInterrupt:
        print("中断信号接收，准备退出...")
    finally:
        if file_watcher.is_alive():
            file_watcher.stop()
            file_watcher.join()
        if reloader.process:
            reloader.process.kill()
            print("脚本进程已终止。")


if __name__ == "__main__":
    main()
