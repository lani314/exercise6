#Write a program, lettercount.py, 
# that opens a file named on the command line 
# and counts how many times each letter occurs in that file. 
# Your program should then print those counts to the screen, 
# in alphabetical order. For example:

from sys import argv

script, inputfile = argv

# creates file object to file can be accessed
lola = open(inputfile)

print "Here's your file %r:" % inputfile

# makes file readable
file_contents = lola.read()

# prints file contents for user to see
print file_contents

# makes all letters low case
new_version = file_contents.lower()

# range for counter, based on ascii
counter=range(0,130)
# begin counter at 0 for each loop
x=0

# loop to go through up to 128
# it errored when i did 130 because out of range
# so did 128
while x <= 128:
	# counter begin at 0
	counter[x]=0
	# counter to iterate/add 1 each time
	x=x+1

# this tests that ascii works
# take lower case version of string
for i in new_version:
	# print i (letter)
	print i 
	# print ASCII equivalent
	print ord(i)
	# counter is ord applied to letters 
	# acounter adds one of ord letters each time
	counter[ord(i)] = counter[ord(i)] + 1

# print counter results
# this will print the results of two loops
# 1) the letters as ord numbers
# 2) the counter of the numbers
print counter
 