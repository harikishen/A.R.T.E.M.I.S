import re
import glob

path="/home/deon/dex/hike-out/com/example/mobilpakket/"
filenames=glob.glob(path+"*.smali")
api=[]
q="\w+\(.*\)"
p=re.compile(q)

for filename in filenames:
	with open(filename,"r") as file:
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

# print(api)



		