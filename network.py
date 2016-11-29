import socket

s = socket.socket()
s.connect(("10.100.0.23", 9999))

s.send(b'sf')
s.send(b"pf")

s.send(b"wu")
s.send(b"qq")

s.close()
