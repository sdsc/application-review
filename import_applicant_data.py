#!/opt/rh/rh-python35/root/usr/bin/python 

import sys
import os
import re
from fnmatch import fnmatch

def NormalizeReply ( reply ):
	switcher = {
		"Outstanding": 5,
		"Excellent": 4,
		"Average": 3,
		"No basis for judgment":-1,
		"No basis for judgement":-1,
	}
	return switcher.get(reply,0)
	
root = "/scratch/slocal/rehs"
pattern = "*Applicant Information*"

dictvalue = 0
EvaluatorDict = {}
for path, subdirs, files in os.walk(root):
	for name in files:
		if fnmatch(name, pattern):
			splitfilename = name.split('-',4)
			splitpath=path.split('/',4)
			chunkname=splitpath[4].split(',',3)
			LastName=chunkname[0].replace(",","")
			tempFirstName=chunkname[1].split(' ',2)
			FirstName=tempFirstName[1]
			ApplicationID = (splitfilename[0])
			fullpath = os.path.join(path, name)

			with open(fullpath) as openfile:
				lines = openfile.readlines()
				referencefrom = 0
				match5 = 0
				match6 = 0
				for nextline in lines:
					if fnmatch(nextline, "5. *"):
						match5 = 1
						continue
					if fnmatch(nextline, "6. *"):
						match5 = 0
						match6 = 1
						continue
					if match5:
						if not nextline.isspace():
							if nextline.strip() == "Female":
								Gender = "F"
							elif nextline.strip() == "Male":
								Gender = "M"
							else:
								Gender = "O"
							print ("INSERT INTO applicant (ApplicationID,FirstName,LastName,Gender) VALUES (",ApplicationID,",\"",FirstName,"\",\"",LastName,"\",\"",Gender,"\");",sep="")
