import os
import glob
import logging
from extract import *
from config import *
from dexparse import *

filenames=glob.glob(path+"*")
index = 0
for filename in filenames:
	dir=filename.split('/')[-1]
	print("dir",dir)
	permissions = extract(dir,index)
	apicalls = dexparse(destinationPath+str(index))
	print(apicalls,permissions)
	index = index + 1
