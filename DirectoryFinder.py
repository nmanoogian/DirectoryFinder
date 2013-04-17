"""
DirectoryFinder
Searches for a specific file using a wordlist and header
"""

from urllib import *
import sys

file = open(sys.argv[1], "r")
line = file.readline()
while line != "":
	url = sys.argv[2]+line.strip().title()
	a=urlopen(url)
	if a.getcode() != 404:
		sys.stderr.write(url)
	print(line.strip())
	line = file.readline()
