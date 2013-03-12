from sys import argv

script, filename = argv
#make file available
f = open(filename)
g = f.read()

print "HERE IS THE FILE:"

#seperate file line by line
for line in f:
	print line

print "HERE IS THE FILE IN LOWER CASE AND A WORD COUNTER:"

now = g.lower()
# make the first letter uppercase

print now

# split the text
splittext = now.split(" ")
print splittext

# set dictionary with key as word(string) and value as count(integer)
my_dict = {}

value = 0
# iterate through words in splittext
# if true, increment by 1
for word in splittext:
	# check if words already in my_dict (true/false?)
	if word in my_dict:
		# if true, add value of 1 to current value of words
		my_dict[word] += 1
	# otherwise, create a new container for word with value of 1	
	else:
		my_dict[word] = 1 #initialize word count
		 #create a new dictionary with keys from seq and values to set to value

# print final result of my_dict
print my_dict		