from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import signal
import time
import subprocess

class WatchdogHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        """Start the Flask app process."""
        print("Starting process...")
        self.process = subprocess.Popen(self.command, shell=True)

    def stop_process(self):
        """Stop the Flask app process."""
        if self.process:
            print("Stopping process...")
            os.kill(self.process.pid, signal.SIGTERM)
            self.process.wait()

    def on_any_event(self, event):
        """Restart Flask app when a file system change occurs."""
        if event.src_path.endswith(".py") or event.src_path.endswith(".html") or event.src_path.endswith(".css"):
            print(f"Detected change in {event.src_path}. Restarting process...")
            self.stop_process()
            self.start_process()

if __name__ == "__main__":
    # Watch current directory, templates folder, and static/css folder
    paths_to_watch = [".", "./templates", "./static/css"]

    command = "flask run"  # Command to run Flask

    event_handler = WatchdogHandler(command)
    observer = Observer()

    # Watch Python, HTML, and CSS files for changes
    for path in paths_to_watch:
        observer.schedule(event_handler, path, recursive=True)

    print(f"Watching for changes in {', '.join(paths_to_watch)}...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
