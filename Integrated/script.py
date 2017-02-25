from os import listdir
import os
from os.path import isfile, join
def dynamic_analysis(filename,location):
	print location
	#mypath = "/home/athulrajts/samples/"
	#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	#for file in onlyfiles:
	os.system("sudo docker run -it --rm -v %s:/samples/:ro -v %s/out:/samples/out honeynet/droidbox /samples/%s 100" %(location,location,filename))
	return True
