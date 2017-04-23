import socket
import sys

HOST, PORT = '127.0.0.1', 3030

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    print('='*50)

except socket.error as msg:
    print("Failed to create socket.\nError code: %s\nError msg: %s"%(str(msg[0]),msg[1]))
    sys.exit(0)
print("Socket created")

while True:
    data = input("text: ")

    if data == ':/quit' or not data:
        sock.close()
        break

    try:
        received = sock.recv(1024)
    finally:
        print('='*50)
        print("Recevied: {}".format(received))
        print('='*50)

    try:
        sock.sendall((data).encode('utf8'))

    finally:
        print('='*50)
        print("Sent:     {}".format(data))
        print('='*50)
