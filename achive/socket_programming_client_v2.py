# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:42:59 2021

@author: tjpin
"""
import socket
import time
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "172.17.10.111"
ADDR = (SERVER, PORT)

sConnected = False

def sockConnection(SERVERADDR):
    global sConnected
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect(SERVERADDR)
        print("Socket server connected.")
        sConnected = True
    except socket.error:
        print("Socket connecting...")
        time.sleep(3)
        sConnected = False
        pass
    return clientSocket
    
def send(socketC, msg):
    global sConnected
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    try:
        socketC.send(send_length)
        socketC.send(message)
        #print(client.recv(2048).decode(FORMAT))
    except socket.error:
        print("Socket disconnected.\nReconnecting...")
        time.sleep(3)
        sConnected = False
        pass

def startSockClient(socketC, ADDR):
    global sConnected
    while True:
        if sConnected == True:
            msg = input()
            send(socketC, msg)
        else:
            socketC = sockConnection(ADDR)
    
    
s = sockConnection(ADDR)
sClientThread = threading.Thread(target=startSockClient, args=(s, ADDR,))
try:
    sClientThread.start()
except:
    print ("Error: unable to start thread")
    
    


        
        
        
        
        