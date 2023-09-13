#!/bin/python3

#python3 scanner.py <ip>

import sys
import socket
from datetime import datetime

#Target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

print("_" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("_" * 50)

try:
	for port in range(1, 100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierro:
	print("Hostname could not be resolved.")

except socket.error:
	print("Could not connect to the server")