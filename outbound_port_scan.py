#! /usr/bin/env python3

import subprocess
import os
import time
successful_results = {}

def port_scan(low_port, high_port):
	website = "portquiz.net:"
	for port_num in range(low_port, high_port):
		port_to_scan = website + "%d" % port_num
		successful_results[port_to_scan] = subprocess.Popen(["wget", "-qO ", 
		port_to_scan])
	output()

def output():
	while successful_results:
		for result1, result2 in successful_results.items():
			if result2.poll() is not None:
				del successful_results[result1]
				if result2.returncode == 0:
# Print string from the 13th index to omit un-needed url text
					print("Port %s is open" % result1[13:])
				elif result2.returncode == 1:
					print("Port %s is blocked" % result1[13:])
				else:
					print("Port %s returns an error" % result1[13:])
				break

def yes_response(resp):
# Check if string is a yes response and return true if so
    YES_RESPONSES = ["y", "yes"]

    resp = resp.lower()

    if resp in YES_RESPONSES:
        return True
    else:
        return False

def main():
	while True:
		try: 
			print("\nThis Programme will scan a range of outbound ports")
			low_port = int(input("\nEnter start port: "))
			high_port = int(input("Enter end port: "))		
			start_time = time.clock()
			port_scan(low_port, high_port)
			end_time = time.clock()
			print("\nScan completed in ", end_time - start_time, " seconds")
		except ValueError:
			print ("\nPlease enter numbers and not letters")
			main()
		if not yes_response(input("\nDo you wish to perform another scan? Y/N : ")):
			break

if __name__=="__main__":
	try:
		main()
# Attempt to make programme exit cleanly
	except KeyboardInterrupt:
		print("\n\nShutdown requested... exiting\n\n")
		try:
			exit()
		except SystemExit:
			os._exit(0)
