import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

path="/home/john/AMD/apk/"
path3="/home/john/AMD/restapk/"
filenames=glob.glob(path+"*")
path2="/home/john/AMD/Android-Malware-Detector"
index = 0
logger.info("extracting apks...")
for filename in filenames:
	dir=filename.split('/')[-1]
	print("dir",dir)
	os.chdir(path)
	os.system("mkdir "+path3+str(index))
	os.system("unzip %s -d %s" %(dir,(path3 + str(index))))
	os.chdir(path2+"/scripts")
	path1="%s%s"%(path3,str(index))
	print("path1",path1)
	os.system(" java -jar /home/john/AMD/Android-Malware-Detector/tools/AXMLPrinter2.jar %s/AndroidManifest.xml >> %s/manifest.txt" %(path1,path1))
	os.system("python manifest_parser.py %s"%(path1))
	index = index +1






