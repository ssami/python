"""

Create cross-os friendly backup script!

"""


import shutil
import os


backupdir = "backup"

try: 
	os.makedirs(backupdir)
except: 
	pass


for f in os.listdir("."): 
	if os.path.splitext(f)[1] == ".py":
		backdest = os.path.join(backupdir, f)
		print """{} to {}""" . format(f, backdest)
		shutil.copy2(f, backdest)
	else: 
		print "Not backing up, not a .py file", f


