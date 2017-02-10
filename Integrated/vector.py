import glob
#import tensorflow as tf
import os
import glob
import logging
from extract import *
from config import *
from dexparse import *
from parse import *
from script import *

file = open('WATCH_LIST')
index = 0
permission_index= {}          # permissions and indices of permissions 
permission_list = file.read().split('\n')   # List of all permissions monitored


for x in permission_list:
	permission_index[x]=index
	index = index+1

file.close()

file = open('SENSITIVE_APIS')
index = 0
apicalls_index = {}
apicalls_list = file.read().split('\n')

for x in apicalls_list:
	apicalls_index[x]=index
	index = index+1
file.close()	

filenames=glob.glob(path+"*")
index = 0
for filename in filenames:
	dir=filename.split('/')[-1]
	print("dir",dir)
	permissions = extract(dir,index)
	apicalls = dexparse(destinationPath+str(index))
	status = dynamic_analysis(dir)
	actions = jsonparse()
	index = index + 1

listing = []
current_app = []
vector =[]
vector_apicalls = []

current_app_permission = permissions
for x in range(0,len(permission_list),1):
	listing.append(0)
for x in current_app_permission:
	if x in permission_index.keys():
		listing[permission_index[x]]=1
vector.append(listing)


listing = []
current_app_apicalls = apicalls
current_app_apicalls.pop()
for x in range(0,len(apicalls_list),1):
	listing.append(0)
for x in current_app_apicalls:
	if x in apicalls_index.keys():
		listing[apicalls_index[x]]=1
vector_apicalls.append(listing)

for x in range(0,len(vector),1):
	vector[x] = vector[x]+vector_apicalls[x]+actions

print(vector[0])
print("\n")  
