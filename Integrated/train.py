from vector import *
from nn import *
from rbm import *
import numpy as np 
from config import *

def createVector(filenames,location):
	global folderindex,vector,label
	for filename in filenames:
		print filename
		temp_vector,temp_label = vectorize(filename,folderindex,location)
		if temp_vector != False:
			vector.append(temp_vector)
			label.append(temp_label)
		folderindex = folderindex +1

folderindex = 0
vector = []
label = []

filenames=glob.glob(path+"*")    # for benign
createVector(filenames,path)
filenames = glob.glob(malpath+"*") #for malware
createVector(filenames,malpath)
#print(vector,label)   

if vector and label:
	trX = np.array(vector,np.float32)
	trY = np.array(label,np.float32)
	RBM_hidden_sizes = [233, 150 ,50]
	inpX = trX
	rbm_list = []
	input_size = inpX.shape[1]
	for i, size in enumerate(RBM_hidden_sizes):
	    print 'RBM: ',i,' ',input_size,'->', size
	    rbm_list.append(RBM(input_size, size))
	    input_size = size
	for rbm in rbm_list:
	    print 'New RBM:'
	    #Train a new one
	    rbm.train(inpX) 
	    #Return the output layer
	    inpX = rbm.rbm_outpt(inpX)
	nNet = NN(RBM_hidden_sizes, trX, trY)
	nNet.load_from_rbms(RBM_hidden_sizes,rbm_list)
	nNet.train()	
	file  = open(vectorstore,"a+")
	for item in vector:
		file.write("[")
		for subitem in item:
	  		file.write("%s," % subitem)
		file.seek(-1, os.SEEK_END)
		file.truncate()
		file.write("],")
	file.seek(-1, os.SEEK_END)
	file.truncate()
	file.close()
else:
	print("Vector Empty")