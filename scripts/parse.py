import json
def jsonparse():
	json_file='/home/athulrajts/samples/out/analysis.json'
	json_data=open(json_file)
	#output = {}
	#output = data
	data = json.load(json_data)
	json_data.close()
	perm = []
	i=0
	#for item in data["accessedfiles"]:
	#	print item
	for item in data:	
		#print item+" 	"+str(len(data[item]))
		perm.append(1 if len(data[item])>0 else 0)
	perm.pop(1)
	return perm 
