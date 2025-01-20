import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    message = input("Enter message ('exit' to quit): ")
    sock.send(message.encode())  
    if message.lower() == 'exit':
        break

    data = sock.recv(1024)
    print(f"Received: {data.decode()}")

sock.close()