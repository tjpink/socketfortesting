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
SERVER = "172.17.10.111"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sconnected = False

while sconnected == False:
    try:
        client.connect(ADDR)
        print("Socket server connected.")
        sconnected = True
    except:
        print("Socket connecting...")
        time.sleep(2)
        pass
    
def send(msg):
    global client
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    try:
        client.send(send_length)
        print("Message sent 1")
        client.send(message)
        print("Message sent 2")
        #print(client.recv(2048).decode(FORMAT))
    except socket.error as msg:
        client.
        #client.close(ADDR)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print (f"Socket Error: {msg}")
        print("Socket connection not establised.\n")
        sconnected = False
        while sconnected == False:
            try:
                print("Socket ")
                client.connect(ADDR)
                print("Socket connected.")
                #resent previous message
                #client.send(send_length)
                #client.send(message)
                sconnected = True
            except socket.timeout:
                time.sleep(2)
                print("reconnecting....\n")
                pass
        pass

while True:
    msg = input()
    send(msg)

            




