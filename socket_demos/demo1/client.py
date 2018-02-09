import socket
HOST = '192.168.0.201'
PORT = 8080

request = 'can you hear me?'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.sendall(request.encode('utf-8'))

response = s.recv(1024)

print('request is:',request)
print('response is:',response.decode('utf-8'))

s.close()