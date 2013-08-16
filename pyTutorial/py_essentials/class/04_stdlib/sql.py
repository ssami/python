#sql.py


import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()

c.execute('''

	create table if not exists employees
	(name text, rank text)

	''')


# must be a list of tuples
employees = [
	("bob", "CEO"), 
	("betty", "CEO level 2"), 
]

c.executemany('''
	insert into employees values (?, ?)
	''', employees)

conn.commit()

# Rowcount CANNOT normally be relied upon for info from a SELECT statement
c.execute("select * from employees")
labels = map(lambda x: x[0], c.description)
print labels

output = []
for row in c: 

	row = zip(labels, row)
	stuff = dict(row)
	#print stuff
	output.append(stuff)

print "Output report for employees", output
for d in output: 
	print "{0[name]} has rank {0[rank]}" . format(d) 		# 0 refers to the argument: that is, from the list in format()


c.execute(''' 
	delete from employees where name = 'bob'
	''')


# Rowcount CANNOT normally be relied upon for info from a SELECT statement
if c.rowcount > 0: 
	print "Yay! Bob is deleted!"
else: 
	print "Oops, something bad happened"
conn.commit()

c.close()
conn.close()