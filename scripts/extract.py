import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

path="/home/deon/apk/"
filenames=glob.glob(path+"*.apk")
path2="/home/deon/Android-Malware-Detector"

logger.info("extracting apks...")
for filename in filenames:
	dir=filename.split('/')[-1].split('.')[0]
	os.chdir(path)
	os.system("mkdir "+dir)
	os.system("unzip %s.apk -d %s" %(dir,dir))
	os.chdir(path2+"/scripts")
	path1="%s/%s"%(path,dir)
	os.system(" java -jar /home/deon/Android-Malware-Detector/tools/AXMLPrinter2.jar %s/AndroidManifest.xml >> %s/manifest.txt" %(path1,path1))
	os.system("python manifest_parser.py %s"%(path1))






