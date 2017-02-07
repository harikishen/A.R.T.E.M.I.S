import glob
import operator
import tensorflow as tf

file = open('testlist.txt')
index = 0
permission_index= {}          # permissions and indices of permissions 
permission_list = file.read().split('\n')   # List of all permissions monitored
extrafile = open("extrafile.txt","a+")

for x in permission_list:
	permission_index[x]=index
	index = index+1
file.close()

listing = []
current_app = []
vector =[]
permission_count = {}   
extra = set()
# vector creation for permissions

for filename in glob.glob("/home/john/Trial/vectorization/permissions/*.txt"):
	file = open(filename)
	listing = []
	print(file)
	current_app_permission = file.read().split('\n')
	for x in range(0,len(permission_list),1):
		listing.append(0)
	for x in current_app_permission:
		if x in permission_index.keys():        #if permissions are present in the testlist of permissions set 1
			listing[permission_index[x]]=1
		else:                                      # if permissions are absent in the testlist add to set extra
			extra.add(x)
	vector.append(listing)
	file.close()

for eachextra in extra:
	extrafile.write(str(eachextra)+"\n")   #writing the set of extra permissions to file extrafile.
    

# tensorflow defintions

sums = tf.constant(vector[0])
for i in range(1,len(vector),1):
	sums = tf.add(sums,tf.constant(vector[i]))    #summing to get total count 

sess = tf.Session()
result = sess.run(sums)

index = 0
for permission in permission_list:              # packing permission with total count 
	permission_count[permission]=result[index]
	index +=1	
sorted_permission_count = sorted(permission_count.items(), key =  operator.itemgetter(1),reverse = True) #
for i in range(len(sorted_permission_count)):  # most frequently used sorted permissions
	if sorted_permission_count[i][1] != 0:
		print(sorted_permission_count[i][0]+" "+str(sorted_permission_count[i][1]))
sess.close()