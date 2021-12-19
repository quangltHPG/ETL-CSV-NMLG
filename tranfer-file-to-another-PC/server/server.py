import socket
import tqdm
import os
import shutil
import datetime

def server_listening():
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5001
    # receive 4096 bytes each time
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"    
    # create the server socket
    # TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))
    # enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(15)
    #s.listen(countSocketListen)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    # accept connection if there is any
    client_socket, address = s.accept() 
    # if below code is executed, that means the sender is connected
    print(f"[+] {address} is connected.")
    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    print ("địa chỉ lưu file: ", filename)
    # convert to integer
    filesize = int(filesize)

    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb", encoding='utf-8') as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    
    # close the client socket
    client_socket.close()
    # close the server socket
    s.close()
    
def processing_file():
    #connect database
    # xử lý file, lưu dữ liệu vào database
    #disconnect database
    return 1
def move_file():
    timeNow = datetime.datetime.now()
    fileName = ""
    pathSourceFile = r"C:\Users\HPDQ\tranfer-file-to-another-PC\server\data.csv"
    pathDesFileDone = r"C:\Users\HPDQ\tranfer-file-to-another-PC\server\data\done"
    fileName = str(timeNow.year) + str(timeNow.month) + str(timeNow.day) + "_"+ str(timeNow.hour) + str(timeNow.minute) + str(timeNow.second)
    pathDesFileDone = os.path.join(pathDesFileDone, fileName + ".csv")
    print (pathDesFileDone)
    shutil.move(pathSourceFile, pathDesFileDone)

while 1:
    try:
        server_listening()
            #temp = processing_file()
            #if temp == 1:
            #    move_file()
    except:
        print ("error", datetime.datetime.now())
        
