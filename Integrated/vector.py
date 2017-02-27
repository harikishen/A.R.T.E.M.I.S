import glob
import tensorflow as tf
import os
import glob
import logging
from config import *
from extract import *
from config import *
from dexparse import *
from parse import *
from script import *

def vectorize(filename,folderindex,location):            #folderindex just a formality..give 0 
	os.chdir(INTEGRATED_PATH)
	file = open('WATCH_LIST')    #file containing the watchlist
	index = 0                     #iterator   
	permission_index= {}          # permissions and indices of permissions 
	permission_list = file.read().split('\n')   # List of all permissions monitored


	for x in permission_list:            #buliding an indexed list or associative array
		permission_index[x]=index
		index = index+1

	file.close()

	file = open('SENSITIVE_APIS')    #file containing the sensitive APIs
	index = 0
	apicalls_index = {}					# API calls and indices 
	apicalls_list = file.read().split('\n')  # List of all API calls monitored

	for x in apicalls_list:       #buliding an indexed list or associative array
		apicalls_index[x]=index   
		index = index+1
	file.close()	

	#filenames=glob.glob(path+"*")    # List of all files apks in to be checked
	vector =[]
	label = []
	vector_apicalls = []
	dir=filename.split('/')[-1]
	print("dir",dir)
	permissions = extract(dir,folderindex,location)       #static analysis
	apicalls = dexparse(destinationPath+str(folderindex)) #static analysis 
 	os.system("sudo rm -r %s"%(destinationPath+str(folderindex)))  #removing extrafolders
	status = dynamic_analysis(dir,location)  #dynamic analysis
	actions = jsonparse(location)  # parsing results of dynamic analysis
	listing = []                   #vectorizing permissions 
	current_app = []
	current_app_permission = permissions
	for x in range(0,len(permission_list),1):
		listing.append(0)         
	for x in current_app_permission:
		if x in permission_index.keys():
			listing[permission_index[x]]=1
	vector.append(listing)       # end of permissions  
	listing = []                      
	current_app_apicalls = apicalls  #vectorizing apicalls
	if current_app_apicalls:                 
		current_app_apicalls.pop()
	for x in range(0,len(apicalls_list),1):
		listing.append(0)
	for x in current_app_apicalls:
		if x in apicalls_index.keys():
			listing[apicalls_index[x]]=1
	vector_apicalls.append(listing)       # end of apicalls  
	for x in range(0,len(vector),1):      # adding actions to it
		if  actions and permissions and apicalls:   # checking if any of above processes failed
			vector[x] = vector[x]+vector_apicalls[x]+actions
			if all(feature == 0 for feature in vector[x]):
				print("All Zeros")
				return False,False
			else:                                       # if all went well, final vector
				if str(location).split('/')[-2] == 'Benign':   
					label.append([0,1])     
				else:
					label.append([1,0])
				file  = open(vectorstore,"a+")
				for item in vector:
					file.write("[")
					for subitem in item:
				  		file.write("%s," % subitem)
					file.seek(-1, os.SEEK_END)
					file.truncate()
					file.write("]\n")
				file.close()
				file = open(labelstore,"a+")
				for item in label:
					file.write("[")
					for subitem in item:
				  		file.write("%s," % subitem)
					file.seek(-1, os.SEEK_END)
					file.truncate()
					file.write("]\n")
				file.close()	
				return vector[0],label[0]
		else:
			return False,False
		#os.chdir(destinationPath)
		#os.system("sh rm -r %s" %(folderindex))


	#file  = open("/home/john/AMD/zdata.txt","a+")
	#for item in vector:
		#file.write("[")
		#for subitem in item:
	  		#file.write("%s," % subitem)
		#file.seek(-1, os.SEEK_END)
		#file.truncate()
		#file.write("],")

	#file.seek(-1, os.SEEK_END)
	#file.truncate()
	#file.close()
	


