import threading
import socket
import threading

nickname = input("Shoose a nickname:")

host = '192.168.50.55'
port = 59000
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'CONN_NAME':
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error has ocvurred")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode(FORMAT))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

