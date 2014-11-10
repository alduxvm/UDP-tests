#####################################################################
# Aldo Vargas
# 
#
# Purpose:
#	Matlab sends n signals via UDP to the Raspberry pie... 
#	RPI receives the data, unpacks it and prints it.
#	- This is just for testing the best methodology between Matlab-rpi
#	This methos uses sockets
#
########################################################################


import SocketServer
import struct
import time

#Raspberry pie IP address
#UDP_IP = "172.30.144.154"
#Mac IP address
UDP_IP = "130.209.27.59"
#UDP_IP = "localhost"
UDP_PORT = 51001


class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
    	udp_mess=""
    	mess=""
    	numOfValues=0
    	timestamp = time.time()
        data = self.request[0].strip()
        socket = self.request[1]
        if data is not None:
	        numOfValues = len(data) / 8
	        mess=struct.unpack('>' + 'd' * numOfValues, data)
	        for x in range(0, numOfValues):
	        	udp_mess = udp_mess+" "+str(mess[x])
	        diff = time.time() - timestamp
	        print str(diff)+udp_mess
	        udp_mess=""


if __name__ == "__main__":
    server = SocketServer.UDPServer((UDP_IP, UDP_PORT), MyUDPHandler)
    print "System ready on "+str(UDP_IP)
    server.serve_forever()
    


