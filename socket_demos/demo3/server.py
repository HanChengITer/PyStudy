# -*- coding:utf-8 -*-
import socket

HOST = '192.168.0.201'
PORT = 8080

index_response = '''HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form> 
</html>
'''

pic_response = '''HTTP/1.x 200 OK  
Content-Type: image/jpg

'''.encode('utf-8')
with open('imgs/header.jpg', 'rb') as pic:
	pic_response += pic.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(3)

while True:
	
	conn,addr=s.accept()
	request = conn.recv(1024).decode('utf-8')
	
	print('request is:',request)
	
	method = None
	if len(request) != 0:
		method = request.split(' ')[0]
		src = request.split(' ')[1]
	
	
	if method == 'GET':
		if src == '/test.jpg':
			response = pic_response
		else:
			response = index_response

		if isinstance(response, str):
			conn.sendall(response.encode('utf-8'))
		else:
			conn.sendall(response)
			
	if method == 'POST':
		form = request.split('\r\n')
		index = form.index("")
		entry = form[index:]
		value = entry[-1].split('=')[-1]
		response = index_response + '\n <p>{}</p>'.format(value)
		if isinstance(response, str):
			conn.sendall(response.encode('utf-8'))
		else:
			conn.sendall(response)

	conn.close()