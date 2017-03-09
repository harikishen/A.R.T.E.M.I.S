import os
import glob
import logging
from config import *
from manifest_parser import *


def extract(dir, index, location):
    os.chdir(location)
    os.system("mkdir " + DEST_PATH + str(index))
    os.system("unzip %s -d %s" % (dir, (DEST_PATH + str(index))))
    os.chdir(SCRIPT_PATH)
    filePath = "%s%s" % (DEST_PATH, str(index))
    print("filePath", filePath)
    os.system(
        " java -jar %s/tools/AXMLPrinter2.jar %s/AndroidManifest.xml >> %s/manifest.txt" %
        (BASE_PATH, filePath, filePath))
    permissions = manifest_parse(filePath)
    return permissions
