import subprocess
import sys
import os
import threading
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

DJANGO_SETTINGS_MODULE = 'config.settings'
WATCH_PATHS = ['.']  # Folders for tracking

patterns = ['*.py', '*.html', '*.env']
ignore_patterns = ['*/migrations/*.py', '*.pyc', '__pycache__']
ignore_directories = False
case_sensitive = False

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

server_process = None


def run_server():
    global server_process
    if server_process:
        print('Stopping the server...')
        server_process.terminate()
        server_process.wait()
    print('Server Startup...')
    server_process = subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver'],
        stdout=sys.stdout,
        stderr=sys.stderr
    )


class ChangeHandler(PatternMatchingEventHandler):
    def on_modified(self, event):
        print(f'Modified file: {event.src_path}')
        run_server()

    def on_created(self, event):
        print(f'Created a file: {event.src_path}')
        run_server()

    def on_deleted(self, event):
        print(f'File deleted: {event.src_path}')
        run_server()


def start_watcher():
    observer = Observer()
    handler = ChangeHandler(
        patterns=patterns,
        ignore_patterns=ignore_patterns,
        ignore_directories=ignore_directories,
        case_sensitive=case_sensitive
    )
    for path in WATCH_PATHS:
        observer.schedule(handler, path=path, recursive=True)
    observer.start()
    return observer


def main():
    run_server()
    observer = start_watcher()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Completions...')
        observer.stop()
        if server_process:
            server_process.terminate()
    observer.join()


if __name__ == '__main__':
    main()
