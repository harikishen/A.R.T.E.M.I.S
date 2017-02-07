import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


path="/home/john/AMD/apk/"                     # Loaction of Input files (APKS allowed)      
destinationPath="/home/john/AMD/restapk/"      # Location to extract to and creation of permissions list
filenames=glob.glob(path+"*")       
scriptPath="/home/john/AMD/Android-Malware-Detector"   #Location of script
index = 0


logger.info("extracting apks...")
for filename in filenames:
	dir=filename.split('/')[-1]
	print("dir",dir)
	os.chdir(path)
	os.system("mkdir "+destinationPath+str(index))
	os.system("unzip %s -d %s" %(dir,(destinationPath + str(index))))
	os.chdir(scriptPath+"/scripts")
	filePath="%s%s"%(destinationPath,str(index))
	print("filePath",filePath)
	os.system(" java -jar /home/john/AMD/Android-Malware-Detector/tools/AXMLPrinter2.jar %s/AndroidManifest.xml >> %s/manifest.txt" %(filePath,filePath))
	os.system("python manifest_parser.py %s"%(filePath))
	index = index +1

print(filenames)




