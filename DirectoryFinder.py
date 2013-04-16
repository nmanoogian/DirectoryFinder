from urllib import *
import sys

file = open(sys.argv[1], "r")
line = file.readline()
while line != "":
	a=urlopen('http://www.cs.rit.edu/~vcss243/Lab/06-Micro'+line.strip())
	print(a.getcode())
