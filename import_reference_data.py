#!/opt/rh/rh-python35/root/usr/bin/python 

import sys
import os
import re
from fnmatch import fnmatch
from reviewerdict import NormalizeEvaluatorName

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
pattern = "*Reference*"

dictvalue = 0
EvaluatorDict = {}
for path, subdirs, files in os.walk(root):
	for name in files:
		if fnmatch(name, pattern):
			splitfilename = name.split('-',4)
			ApplicationID = (splitfilename[0])
			ReferenceID = (splitfilename[2])
			fullpath = os.path.join(path, name)
			print ("INSERT INTO reference (ApplicationID,ReferenceID) VALUES (",ApplicationID,",",ReferenceID,");")

			with open(fullpath) as openfile:
				lines = openfile.readlines()
				referencefrom = 0
				match2 = 0
				match3 = 0
				match6 = 0
				match7 = 0
				match8 = 0
				match9 = 0
				match10 = 0
				match11 = 0
				match12 = 0
				match13 = 0
				match14 = 0
				match15 = 0
				match16 = 0
				match17 = 0
				match18 = 0
				match19 = 0
				linecount = 0
				commentline = ""
				for nextline in lines:
					linecount += 1
					# section 7
					if fnmatch(nextline, "Reference from:*"):
						referencefrom = 1
						continue
					if fnmatch(nextline, "2. *"):
						referencefrom = 0
						match2 = 1
						continue
					if fnmatch(nextline, "3. *"):
						match2 = 0
						match3 = 1
						continue
					if fnmatch(nextline, "7. *"):
						match6 = 0
						match7 = 1
						continue
					elif fnmatch(nextline, "8. *"):
						match7 = 0
						match8 = 1
						continue
					elif fnmatch(nextline, "9. *"):
						match8 = 0
						match9 = 1
						continue
					elif fnmatch(nextline, "10. *"):
						match9 = 0
						match10 = 1
						continue
					elif fnmatch(nextline, "11. *"):
						match10 = 0
						match11 = 1
						continue
					elif fnmatch(nextline, "12. *"):
						match11 = 0
						match12 = 1
						continue
					elif fnmatch(nextline, "13. *"):
						match12 = 0
						match13 = 1
						continue
					elif fnmatch(nextline, "14. *"):
						match13 = 0
						match14 = 1
						continue
					elif fnmatch(nextline, "15. *"):
						match14 = 0
						match15 = 1
						continue
					elif fnmatch(nextline, "16. *"):
						match15 = 0
						match16 = 1
						continue
					elif fnmatch(nextline, "17. *"):
						match16 = 0
						match17 = 1
						continue
					elif fnmatch(nextline, "18. *"):
						match17 = 0
						match18 = 1
						continue
					elif fnmatch(nextline, "19. *"):
						match18 = 0
						match19 = 1
						continue
					if referencefrom:
						EvaluatorName = nextline.strip()
						EvaluatorName = NormalizeEvaluatorName( EvaluatorName )
						if EvaluatorName not in EvaluatorDict:
							EvaluatorDict[EvaluatorName] = dictvalue
							CurrentEvaluatorID = dictvalue
							print ("INSERT INTO evaluator (EvaluatorID,Name) VALUES (",CurrentEvaluatorID,",\"",EvaluatorName,"\");", sep="")
							dictvalue += 1	
						else:
							CurrentEvaluatorID = EvaluatorDict[EvaluatorName]
						referencefrom = 0
						print ("UPDATE reference SET EvaluatorID=",CurrentEvaluatorID," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match7:
						if not nextline.isspace():
							print ("UPDATE reference SET Q7=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match8:
						if not nextline.isspace():
							print ("UPDATE reference SET Q8=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match9:
						if not nextline.isspace():
							print ("UPDATE reference SET Q9=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match10:
						if not nextline.isspace():
							print ("UPDATE reference SET Q10=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match11:
						if not nextline.isspace():
							print ("UPDATE reference SET Q11=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match12:
						if not nextline.isspace():
							print ("UPDATE reference SET Q12=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match13:
						if not nextline.isspace():
							print ("UPDATE reference SET Q13=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match14:
						if not nextline.isspace():
							print ("UPDATE reference SET Q14=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match15:
						if not nextline.isspace():
							print ("UPDATE reference SET Q15=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match16:
						if not nextline.isspace():
							print ("UPDATE reference SET Q16=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match17:
						if not nextline.isspace():
							print ("UPDATE reference SET Q17=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match18:
						if not nextline.isspace():
							print ("UPDATE reference SET Q18=",NormalizeReply(nextline.strip())," WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
					if match19:
						commentline += nextline.replace("\"","\\\"").replace("?","\'")
			print ("UPDATE reference SET Comments=\"",commentline,"\" WHERE ApplicationID=",ApplicationID," AND ReferenceID=",ReferenceID,";")
