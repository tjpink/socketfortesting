import socket
import time
import threading

HEADER = 128
PORT = 59000
FORMAT = 'utf-8'
SERVER = "192.168.180.210"
ADDR = (SERVER, PORT)

connName = 'CONN_NAME: VISION_DETECTION'

def sockConnection():
    global clientSocket
    global ADDR
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sConnected = False
    while sConnected == False:
        try:
            clientSocket.connect(ADDR)
            print("Socket server connected.")
            sConnected = True
        except socket.error:
            print("Socket connecting...")
            time.sleep(3)
            pass


def receive():
    while True:
        try:
            message = clientSocket.recv(HEADER).decode(FORMAT)
            if message == 'CONN_NAME':
                clientSocket.send(connName.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error has ocurred")
            break
    
def send(msg):
    global clientSocket
    message = msg.encode(FORMAT)
    try:
        clientSocket.send(message)
    except socket.error:
        print("Socket disconnected.\nReconnecting...")
        time.sleep(3)
        sockConnection()
        pass
    
    
sockConnection()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

while True:
    message = input("Enter a string: ")    
    send(message)