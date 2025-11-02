# udp_chat.py
import socket

# ----- SERVER -----
def udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 9000))
    print("UDP Server listening...")
    while True:
        data, addr = s.recvfrom(1024)
        print("Client:", data.decode())
        msg = input("Server: ")
        s.sendto(msg.encode(), addr)

# ----- CLIENT -----
def udp_client():
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('localhost', 9000)
    while True:
        msg = input("Client: ")
        c.sendto(msg.encode(), server)
        if msg.lower() == 'exit':
            break
        data, _ = c.recvfrom(1024)
        print("Server:", data.decode())
    c.close()
