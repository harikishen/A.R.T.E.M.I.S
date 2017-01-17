import re
import glob
import os
from config import *

api=[]
os.chdir(APP_FOLDER)
os.system("sh %sd2j-baksmali.sh %sclasses.dex" %(DEX2SMALI_PATH,APP_FOLDER))

for root, dirs, files in os.walk(APP_FOLDER+"classes-out/"):
	for filename in files:
		if filename.endswith((".smali")):
			regex="\w+\(.*\)"
			pattern=re.compile(regex)
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

						match=pattern.search(function)
						if match:
							function=function.split('(')[0]
							api.append(classname+";->"+function+"()")
							
print api



		