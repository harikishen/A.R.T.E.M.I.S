import glob
import tensorflow as tf

file = open('WATCH_LIST')
index = 0
permission_index= {}          # permissions and indices of permissions 
permission_list = file.read().split('\n')   # List of all permissions monitored


for x in permission_list:
	permission_index[x]=index
	index = index+1

file.close()

file = open('apicalls.txt')
index = 0
apicalls_index = {}   # apicalls and indices of apicalls 
apicalls_list = file.read().split('\n')  # List of all apicalls monitored


for x in apicalls_list:
	apicalls_index[x] = index
	index = index+1

file.close()


listing = []
current_app = []
vector =[]
vector_apicalls = []

for filename in glob.glob("/home/john/Trial/vectorization/permissions/*.txt"):
	file = open(filename)
	listing = []
	current_app_permission = file.read().split('\n')
	for x in range(0,len(permission_list),1):
		listing.append(0)
	for x in current_app_permission:
		if x in permission_index.keys():
			listing[permission_index[x]]=1
	vector.append(listing)
	file.close()

for filename in glob.glob("/home/john/Trial/vectorization/apicalls/*.txt"):
	file = open(filename)
	listing = []
	current_app_apicalls = file.read().split('\n')
	current_app_apicalls.pop()
	for x in range(0,len(apicalls_list),1):
		listing.append(0)
	for x in current_app_apicalls:
		listing[apicalls_index[x]]=1
	vector_apicalls.append(listing)
	file.close()
for x in range(0,len(vector),1):
	vector[x] = vector[x]+vector_apicalls[x]



mat1 = tf.constant(vector[0])
mat2 =  tf.constant(vector[1])
sums = tf.add(mat1,mat2)

sess = tf.Session()

result =  sess.run(sums)
print(vector[1],vector_apicalls[1])
print("\n")
print(vector[0],vector_apicalls[0])
print("\n")
print(result)
sess.close()