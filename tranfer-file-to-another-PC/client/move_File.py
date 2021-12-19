import shutil
import datetime
import os
pathSourceFile = r"C:\Users\HPDQ\tranfer-file-2\\data\in\data.csv"
pathDesFile = r"C:\Users\HPDQ\tranfer-file-2\data\done"

def moveFile(pathSourceFile, PathDesFile):
    
    #pathDesFileFailer = r"C:\Users\HPDQ\tranfer-file-to-another-PC\server\data\failer"

    timeNow = datetime.datetime.now()
    fileName = ""
    fileName = str(timeNow.year) + str(timeNow.month) + str(timeNow.day) + "_"+ str(timeNow.hour) + str(timeNow.minute) + str(timeNow.second)
    print ("ten file: ", fileName)
    PathDesFile = os.path.join(PathDesFile, fileName + ".csv")
    print (PathDesFile, "\n", pathSourceFile)
    shutil.move(pathSourceFile, PathDesFile)
if __name__ == "__main__":
    moveFile(pathSourceFile, pathDesFile)