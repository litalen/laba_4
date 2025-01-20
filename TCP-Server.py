import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

print("Server is listening on port 9090...") 
conn, addr = sock.accept()
print(f"Connection from: {addr}") 
try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode().strip() 
        if message.lower() == 'exit':
             print("Client disconnected.") 
             break
        conn.send(message.upper().encode())
finally:
    conn.close()
    sock.close() 
    print("Server closed.")