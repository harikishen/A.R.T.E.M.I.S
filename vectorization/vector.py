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

listing = []
current_app = []
vector =[]

for filename in glob.glob("/home/john/Trial/vectorization/permissions/*.txt"):
	file = open(filename)
	print(file)
	listing = []
	current_app_permission = file.read().split('\n')
	for x in range(0,len(permission_list),1):
		listing.append(0)
	for x in current_app_permission:
		if x in permission_index.keys():
			listing[permission_index[x]]=1
	vector.append(listing)
	file.close()

sums = tf.constant(vector[0])
for x in range(len(vector)-1):
	mat = tf.constant(vector[x+1])
	sums = tf.add(sums,mat)

sess = tf.Session()

result =  sess.run(sums)
print(vector[1])
print("\n")
print(vector[0])
print("\n")
print(result)
sess.close()