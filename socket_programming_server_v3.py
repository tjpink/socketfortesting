import socket 
import ros_helper
import threading

# Lists For Clients and Their Nicknames
conns = []
connNames = []

HEADER = 128
PORT = 59000

#start server
SERVER = socket.gethostbyname(socket.gethostname() + ".local")
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Sending Messages To All Connected Clients
def broadcast(message):
    for conn in conns:
        conn.send(message)

#handling messages from clients
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    imageMsg = False
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg == '!DISCONNECT':
            connected = False
            print("Socket connection closed")
            conn.send("Socket connection terminated.".encode(FORMAT))
        print(f"[{addr}] {msg}")          
        conn.send("Msg received".encode(FORMAT))
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        # Request And Store Nickname
        conn.send('CONN_NAME'.encode(FORMAT))
        connName = conn.recv(HEADER).decode(FORMAT)
        connNames.append(connName)
        conns.append(conn)

        # Print And Broadcast Nickname
        print("Conn name is {}".format(connName))
        broadcast("{} joined!".format(connName).encode(FORMAT))
        conn.send('Connected to server!'.encode(FORMAT))
        
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
server_Thread = threading.Thread(target=start)
server_Thread.start()


if __name__ == "__main__":
    while True:
        value = input("Please enter a string: ")
        print(f'You have entered {value}')
        broadcast(value.encode(FORMAT))



