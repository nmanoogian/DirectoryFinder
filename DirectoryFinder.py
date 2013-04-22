"""
DirectoryFinder
Author: Nicolas Manoogian <njm7461@cs.rit.edu>
Date: April 21, 2013
Desc: Searches for a specific file using a wordlist and header
"""

from urllib import *
import sys
# If there are only 2 command line arguments: one list
if len(sys.argv) == 3:
	file = open(sys.argv[1], "r")
	line = file.readline()
	while line != "":
		url = sys.argv[2]+line.strip().title()
		a=urlopen(url)
		if a.getcode() != 404:
			# Write successful URLs to Standard Err
			sys.stderr.write(url)
		print(line.strip())
		line = file.readline()
# There are 3 command line arguments: two lists
else:
	file1 = open(sys.argv[1], "r")
	line1 = file1.readline()
	while line1 != "":
		file2 = open(sys.argv[2], "r")
		line2 = file2.readline()
		while line2 != "":
                	url = sys.argv[3]+line1.strip().title()+"-"+line2.strip().title()
			a=urlopen(url)
                	if a.getcode() != 404:
				# Write successful URLs to Standard Err
                	        sys.stderr.write(url)
                	print(url)
                	line2 = file2.readline()
		line1 = file1.readline()
