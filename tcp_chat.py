# tcp_chat.py
import socket

# ----- SERVER -----
def tcp_server():
    s = socket.socket()
    s.bind(('localhost', 8000))
    s.listen(1)
    print("TCP Server waiting for connection...")
    conn, addr = s.accept()
    print("Connected to", addr)
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            break
        print("Client:", data)
        msg = input("Server: ")
        conn.send(msg.encode())
    conn.close()
    s.close()

# ----- CLIENT -----
def tcp_client():
    c = socket.socket()
    c.connect(('localhost', 8000))
    print("Connected to server. Type 'exit' to quit.")
    while True:
        msg = input("Client: ")
        c.send(msg.encode())
        if msg.lower() == 'exit':
            break
        print("Server:", c.recv(1024).decode())
    c.close()
