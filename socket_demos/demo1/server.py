import socket

HOST = '192.168.0.201'
PORT = 8080

response = "Yes"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen(3)
conn,addr=s.accept()
request = conn.recv(1024)

print('request is:', request)
print('connected by:',addr)

conn.sendall(response.encode('utf-8'))

conn.close()