import os
import glob
import logging
from config import *
from manifest_parser import *

def extract(dir,index,location):
	os.chdir(location)
	os.system("mkdir "+destinationPath+str(index))
	os.system("unzip %s -d %s" %(dir,(destinationPath + str(index))))
	os.chdir(SCRIPT_PATH)
	filePath="%s%s"%(destinationPath,str(index))
	print("filePath",filePath)
	os.system(" java -jar %s/tools/AXMLPrinter2.jar %s/AndroidManifest.xml >> %s/manifest.txt" %(basePath,filePath,filePath))
	permissions = manifest_parse(filePath)
	return permissions





