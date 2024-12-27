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


class PythonScriptWatcher:
    """A utility to monitor Python scripts for changes and automatically restart them."""

    process: Optional[Popen] = None
    restart_timer: Optional[Timer] = None

    def __init__(self, script_path: str):
        self.script_path = script_path
        atexit.register(self.cleanup)

    def start_script(self):
        """Start or restart the target Python script."""
        if self.process:
            self.log_event("Restarting script...", "yellow")
            self.process.terminate()
            self.process.wait()

        self.log_event("Starting new script process...", "green")
        self.process = Popen(["python", self.script_path])

    def initialize_file_watcher(self, watched_directory: str):
        """Set up the file watcher to monitor changes in the specified directory."""
        self.log_event("Setting up file watcher...", "blue")
        file_event_handler = PatternMatchingEventHandler(patterns=["*.py"])
        setattr(file_event_handler, "on_modified", self.on_file_change_detected)

        file_watcher = Observer()
        file_watcher.schedule(file_event_handler, watched_directory, recursive=True)
        return file_watcher

    def on_file_change_detected(self, event):
        """Handle file modification events by restarting the script."""
        if self.restart_timer:
            self.restart_timer.cancel()

        self.log_event(f"File changed: {event.src_path}", "magenta")
        self.restart_timer = Timer(1, self.start_script)
        self.restart_timer.start()

    def cleanup(self):
        """Clean up resources on exit."""
        if self.process:
            self.log_event("Cleaning up script process...", "red")
            self.process.terminate()
            self.process.wait()
        if self.restart_timer:
            self.restart_timer.cancel()

    @staticmethod
    def log_event(message: str, color: str):
        """Unified method for logging events."""
        console.log(f"[{color}]{message}[/{color}]")


def main():
    if len(sys.argv) < 3:
        console.log(
            "[red]Usage: python reloadable.py <script_file_path> <watched_directory>[/red]"
        )
        return

    script_file_path = sys.argv[1]
    watched_directory = sys.argv[2]

    watcher = PythonScriptWatcher(script_file_path)
    watcher.start_script()
    file_watcher = watcher.initialize_file_watcher(watched_directory)

    def handle_exit(signum, frame):
        console.log("[red]Interrupt signal received. Exiting...[/red]")
        file_watcher.stop()

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    try:
        file_watcher.start()
        console.log("[green]File watcher started. Monitoring changes...[/green]")
        while file_watcher.is_alive():
            file_watcher.join(1)
    finally:
        watcher.cleanup()
        console.log("[blue]PythonScriptWatcher terminated.[/blue]")


if __name__ == "__main__":
    main()
