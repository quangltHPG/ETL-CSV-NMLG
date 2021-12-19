import socket
import tqdm
import os

def client_speaking(filename):
    #pathData = r"D:\duLieuVanHanh\client\data\in"
    #fileName = "data.csv"
    #filename = os.path.join(pathData,fileName)

    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    host = "192.168.113.35"
    port = 5001



    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    print ("file name: ", filename)
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode('utf-8'))

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb", encoding='utf-8') as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
    return 1
