from urllib import *
import sys

file = open(sys.argv[1], "r")
line = file.readline()
while line != "":
	url = sys.argv[2]+line.strip().title()
	a=urlopen(url)
	if a.getcode() != 404:
		print(url)
	# print(line.strip())
	line = file.readline()
