# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:42:59 2021

@author: tjpin
"""
import socket
import time

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.50.55"
ADDR = (SERVER, PORT)

clientSocket = clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    
def send(msg):
    global clientSocket
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #append " " the rest of the 64 bytes to the first length message
    send_length += b' ' * (HEADER - len(send_length)) 
    try:
        clientSocket.send(send_length)
        clientSocket.send(message)
        print(clientSocket.recv(2048).decode(FORMAT))
    except socket.error:
        print("Socket disconnected.\nReconnecting...")
        time.sleep(3)
        sockConnection()
        pass
    
    
sockConnection()
while True:
    message = input("Enter a string: ")    
    if message == "image" :
        send(message)
        with open("/home/tjpink/Pictures/tinyant.png", "rb") as file:
            imageData = file.read(1024)
            while imageData:
                clientSocket.send(imageData)
                # print(f"Sent {imageData!r}")
                imageData = file.read(1024)
        file.close()
    else :
        send(message)



    
    


        
        
        
        
        
