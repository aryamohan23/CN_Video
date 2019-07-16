import socket
import cv2
import numpy as np
import sys
import time

if(len(sys.argv) != 3):
    print("Usage : {} hostname port".format(sys.argv[0]))
    print("e.g.   {} 192.168.0.39 1080".format(sys.argv[0]))
    sys.exit(-1)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creates 'clientsocket' AF_INET means IPv4
host = sys.argv[1]
port = int(sys.argv[2])
server_address = (host, port)

while(True):
    sent = sock.sendto("get".encode('utf-8'), server_address)
    data, server = sock.recvfrom(65535) #buffersize is 65535 which is max size of jpg image
    print("Fragment size : {}".format(len(data)))
    if len(data) == 4:
        if(data == "FAIL"):
            continue
    array = np.frombuffer(data, dtype=np.dtype('uint8')) #converts into a 1D array and takes the data in the data type uint8
    img = cv2.imdecode(array, 1)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Asking the server to quit")
        sock.sendto("quit".encode('utf-8'), server_address)
        print("Quitting")
        break









