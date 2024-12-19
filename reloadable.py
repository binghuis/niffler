from subprocess import Popen
from sys import argv
from threading import Timer

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

SCRIPT_FILENAME = argv[1]


class Runner:
    __proc = None
    __handler_func = None

    @staticmethod
    def run():
        Runner.__proc = Popen(["python", SCRIPT_FILENAME])

    @staticmethod
    def handle_file_modified(event):
        if Runner.__proc:
            Runner.__proc.kill()
        if Runner.__handler_func:
            Runner.__handler_func.cancel()
        Runner.__handler_func = Timer(1, Runner.run)
        Runner.__handler_func.start()


def setup_watcher():
    event_handler = PatternMatchingEventHandler(patterns=["*.py"])
    event_handler.on_modified = Runner.handle_file_modified

    watcher = Observer()
    watcher.schedule(event_handler, "./src/niffler", recursive=True)
    return watcher


def main():
    Runner.run()
    file_watcher = setup_watcher()

    try:
        file_watcher.start()
        while file_watcher.is_alive():
            file_watcher.join(1)
    except KeyboardInterrupt:
        file_watcher.stop()
    finally:
        file_watcher.join()


if __name__ == "__main__":
    main()
