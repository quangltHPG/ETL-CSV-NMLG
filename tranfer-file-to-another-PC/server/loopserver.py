import shutil
import time 
import datetime
import os

from server import server_listening
pathSourceFile = r"C:\Users\HPDQ\tranfer-file-to-another-PC\server\data.csv"
pathDesFileDone = r"C:\Users\HPDQ\tranfer-file-to-another-PC\server\data\done"
pathDesFileFailer = r"C:\Users\HPDQ\tranfer-file-to-another-PC\server\data\failer"


timeNow = datetime.datetime.now()
fileName = ""
'''fileName = str(timeNow.year) + str(timeNow.month) + str(timeNow.day) + "_"+ str(timeNow.hour) + str(timeNow.minute) + str(timeNow.second) + ".csv"
#print(fileName)
pathDesFileDone = os.path.join(pathDesFileDone, fileName)
print (pathDesFileDone)'''
while 1:
    fileName = ""
    print ("file name :", fileName)
    server_listening()
    fileName = str(timeNow.year) + str(timeNow.month) + str(timeNow.day) + "_"+ str(timeNow.hour) + str(timeNow.minute) + str(timeNow.second)   
    #print(fileName)
    pathDesFileDone = os.path.join(pathDesFileDone, fileName + ".csv")
    print (pathDesFileDone)
    #progress receiving ?
    shutil.move(pathSourceFile, pathDesFileDone)