import re
import glob
import os
from config import *

appfolder="/home/deon/apk/apks/hike/"
os.chdir(appfolder)
os.system("sh %sd2j-baksmali.sh %sclasses.dex" %(DEX2SMALI_PATH,appfolder))

for root, dirs, files in os.walk(appfolder+"classes-out/"):
	for filename in files:
		if filename.endswith((".smali")):
			q="\w+\(.*\)"
			p=re.compile(q)
			file_path=os.path.join(root, filename)
			with open(file_path,"r") as file:
				for line in file:
					line=line.replace('\n',"")
					line=line.replace('\t',"")
					splitline=line.split(" ")[-1]
						
					if len(splitline.split(';->'))>=2:
						function=splitline.split(';->')[-1]
						classname=splitline.split(';->')[0]

						classname=classname.split('/')[-1]

						m=p.search(function)
						if m:
							function=function.split('(')[0]
							# api.append(classname+";->"+function+"()")
							print(classname+";->"+function+"()")

# filenames=glob.glob(path+"*.smali")
# api=[]
# q="\w+\(.*\)"
# p=re.compile(q)

# for filename in filenames:
# 	with open(filename,"r") as file:
# 		for line in file:
# 			line=line.replace('\n',"")
# 			line=line.replace('\t',"")
# 			splitline=line.split(" ")[-1]
			
# 			if len(splitline.split(';->'))>=2:
# 				function=splitline.split(';->')[-1]
# 				classname=splitline.split(';->')[0]

# 				classname=classname.split('/')[-1]

# 				m=p.search(function)
# 				if m:
# 					function=function.split('(')[0]
# 					# api.append(classname+";->"+function+"()")
# 					print(classname+";->"+function+"()")





		