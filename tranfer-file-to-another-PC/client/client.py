from move_File import moveFile
from clientSpeaking import client_speaking
import os
import datetime
import shutil
pathTrigger = r"D:\duLieuVanHanh\client\data\trigger.txt"
pathSourceFile = r"D:\duLieuVanHanh\client\data\in\data.csv"
pathDesFileDone = r"D:\duLieuVanHanh\client\data\done"
pathDesFileFailer = r"D:\duLieuVanHanh\client\data\failer\data.csv"

while True:
    with open(pathTrigger, 'r') as f:
        trigger = f.readline()
        arrTrigger = trigger.split()
        print (arrTrigger)
        if arrTrigger[0] == "create":
            pathFile = arrTrigger[1]
            try:
                _client_speaking = client_speaking(pathSourceFile)
            except:
                _client_speaking = 0
            if _client_speaking == 1:
                moveFile(pathSourceFile, pathDesFileDone)
            else:
                moveFile(pathSourceFile, pathDesFileFailer)
        else:
            moveFile(pathSourceFile, pathDesFileFailer)
