from urllib import *

file = open("words.li", "r")
line = file.readline()
while line != "":
	a=urlopen('http://www.cs.rit.edu/~vcss243/Lab/06-Micro'+line.strip())
	print(a.getcode())
