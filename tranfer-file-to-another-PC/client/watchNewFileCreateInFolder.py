import shutil
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#import datetime
#timeNow = datetime.datetime.now()
import os

path = r"D:\duLieuVanHanh\client\data\in"
#pathNewFile = r"C:\Users\HPDQ\tranfer-file-to-another-PC\client\data\in\data.csv"
#pathSourceFile = r"C:\Users\HPDQ\tranfer-file-to-another-PC\client\data\in\data.csv"


class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        # do something, eg. call your function to process the image
        print ("Got event for file %s" % event.src_path)
        return 1

observer = Observer()
event_handler = ExampleHandler() # create event handler
print (event_handler)
    # set observer to use created handler in directory
observer.schedule(event_handler, path)
observer.start()
    #print (observer.schedule(event_handler, path ))

    # sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
