from os import path
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import datetime

pathLog = r"D:\duLieuVanHanh\client\data\log.txt"
pathTrigger = r"D:\duLieuVanHanh\client\data\trigger.txt"
def on_created(event):
#    print(f"hey, {event.src_path} has been created!")
    with open(pathLog, 'a') as f:
        temp = []
        temp = ['create ', {event.src_path}, ' ', datetime.datetime.now(), '\n']
        for i in temp:
            f.write(str(i))
    with open(pathTrigger, 'w') as f:
        temp = []
        temp = ['create ', event.src_path, ' ', datetime.datetime.now(), '\n']
        for i in temp:
            f.write(str(i))

def on_deleted(event):
#    print(f"what the f**k! Someone deleted {event.src_path}!")
    with open(pathLog, 'a') as f:
        temp = []
        temp = ['deleted ', {event.src_path}, ' ', datetime.datetime.now(), '\n']
        for i in temp:
            f.write(str(i))
def on_modified(event):
#    print(f"hey buddy, {event.src_path} has been modified")
    with open(pathLog, 'a') as f:
        temp = []
        temp = ['modified ', {event.src_path}, ' ', datetime.datetime.now(), '\n']
        for i in temp:
            f.write(str(i))
def on_moved(event):
#    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    with open(pathLog, 'a') as f:
        temp = []
        temp = ['move ', {event.src_path}, ' ', datetime.datetime.now(), '\n']
        for i in temp:
            f.write(str(i))
if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved
    path = r"D:\duLieuVanHanh\client\data\in"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()