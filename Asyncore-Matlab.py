#####################################################################
# Aldo Vargas
# 
#
# Purpose:
#	Matlab sends n signals via UDP to the Raspberry pie... 
#	RPI receives the data, unpacks it and prints it.
#	- This is just for testing the best methodology between Matlab-rpi -
#	This methos uses the asynchronous socket handler module
#
########################################################################


import asyncore
import socket
import struct
import timeit

#Raspberry pie IP address
#UDP_IP = "172.30.144.154"
UDP_IP = "localhost"
UDP_PORT = 51001

class AsyncoreServerUDP(asyncore.dispatcher):
	def __init__(self):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.bind((UDP_IP, UDP_PORT))
	
	#Even though UDP is connectionless this is called when it binds to a port
	def handle_connect(self):	
		print "Server Started..."

	# This is called everytime there is something to read
	def handle_read(self):
		udp_mess=""
		timestamp = timeit.default_timer()
		data, addr = self.recvfrom(2048)
		numOfValues = len(data) / 8
		mess=struct.unpack('>' + 'd' * numOfValues, data)
		for x in range(0, numOfValues):
 			udp_mess = udp_mess+" "+str(mess[x])
 		diff = timeit.default_timer() - timestamp
 		print str(diff)+udp_mess

	# This is called all the time and causes errors if you leave it out.
	def handle_write(self):
		pass

AsyncoreServerUDP()
asyncore.loop()