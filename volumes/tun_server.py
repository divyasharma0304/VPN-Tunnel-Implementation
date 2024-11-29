#!/usr/bin/python3

from scapy.all import *

#Create UDP socket for receive
IP_A = "0.0.0.0"
PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_A, PORT))

while True:
	data, (ip, port) = sock.recvfrom(2048)
	print("{}:{} --> {}:{}".format(ip, port, IP_A, PORT))
	pkt = IP(data)
	print("From sock Inside: {} --> {}".format(pkt.src, pkt.dst))
		
