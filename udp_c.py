import socket

UDP_IP="10.0.0.1"
UDP_PORT=5005
MESSAGE=0


print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while MESSAGE < 3000:
	MESSAGE += 1
	print "message: ", MESSAGE
	sock.sendto(str(MESSAGE) + ""*100, (UDP_IP, UDP_PORT))