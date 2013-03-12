from sys import argv

script, filename = argv
#make file available
f = open(filename)

#seperate file line by line
for line in f:
	print line
# split the text

print "Now, in lower case!"

now = line.lower()
# make the first letter uppercase

print now

splittext = now.split(" ")
print splittext

# set dictionary with key as word(string) and value as count(integer)
my_dict = {}

value = 0
# iterate through words in splittext
# check if words already in my_dict (true/false?)
# if true, increment by 1
# if false, add word and increment by 1
for word in splittext:
	if word in my_dict:
		# increment 
		my_dict[word] += 1
	else:
		my_dict[word] = 1 #initialize word count
		my_dict[word] = 'newvalue'

print my_dict		