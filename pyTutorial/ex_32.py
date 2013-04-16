the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count : 
	print "This is count %d" % number

for fruit in fruits : 
	print "This is fruit of type: %s" % fruit

for i in change : 
	print "I got %r" % i

elements = []
for i in range(45, 62) : 
	print "Adding %d to the list" % i 
	elements.append(i)

for i in elements : 
	print "Element was %d " % i 

elements2 = [
[1, 2, 3, 4],
['apples', 'pears', 'banana']
]

for i in elements2 : 
	print "This is: %r " % i 

print elements2[1][2]

