# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:41:28 2021

@author: tjpin
"""
import socket 
import ros_helper
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname() + ".local")
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    imageMsg = False
    while connected:
        if imageMsg == False : 
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print("Socket connection closed")
                    conn.send("Socket connection terminated.".encode(FORMAT))
                if msg == "image" :
                    imageMsg = True
                print(f"[{addr}] {msg}")          
                conn.send("Msg received".encode(FORMAT))
        else :
            imageMsg = False
            with open("image_received.png", "wb") as file:
                while True:
                    image_chunk = conn.recv(1024)
                    if not image_chunk:
                        break
                    file.write(image_chunk)
            print("Got the file")
            file.close()
            print ("here2\n")
            server.send("Image received".encode(FORMAT))
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
server_Thread = threading.Thread(target=start)
server_Thread.start()

#print("ros_helper.py activating")
#roshelper_Thread = threading.Thread(target=)
#roshelper_Thread.start()

def getDepthsFromAngles(angles):
    ros_helper.pub_angles_to_ros(angles)
    d = ros_helper.getDepths()
    ros_helper.clearPreviousDepths()
    return d 

if __name__ == "__main__":
    while True:
        value = input("Please enter a string: ")
        print(f'You have entered {value}')



