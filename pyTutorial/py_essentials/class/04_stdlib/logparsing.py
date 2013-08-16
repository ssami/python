
# We need to make files with a number in them 

import re
import os


dirname = "logs"
try: 
	os.mkdir(dirname)
except: 
	pass


filename = "xyz"
for n in range(1, 6):
	f = "%s0%s" % (filename, n)
	f = os.path.join(dirname, f)
	fh = open(f, "w")

	for i in range(0, 100):
		fh.write("0%s\n" % n)

	fh.close()


# We want to get each file in samplefiles 
# Increment the numbers in the file

list_of_files = []
for f in os.listdir(dirname):
	if f.find("xyz") != -1: 
		list_of_files.append(f)

# Increment in reverse so that we don't overwrite files

list_of_files.sort()
list_of_files.reverse()


# increment number in file name and in files
for f in list_of_files:
	prev_number = re.search(r"(\d+)", f)
	if prev_number: 
		next_number = int(prev_number.group(1))
		print next_number
		next_number += 1
		next_number = str(next_number).zfill(2)
		prev_number = prev_number.group(1)
		#open file
		#iterate each line, changing all prev num to next num
		#write lines to new file
		#unlink delete the old file
		f_old = open(os.path.join(dirname, f), "r")
		f_new = open(os.path.join(dirname, filename) + next_number, "w")
		for line in f_old: 
			line = line.replace(prev_number, next_number)				# remember, STRINGS ARE IMMUTABLE!
			f_new.write(line)
		f_old.close()
		os.unlink(os.path.join(dirname, f))
		f_new.close()
	else: 
		exit(121)
