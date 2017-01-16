from bs4 import BeautifulSoup
import sys


path=sys.argv[1]
pathlist = path.split("/")
index =pathlist.pop()
print(" list ::: ",pathlist)
pathlist = "/".join(pathlist)
infile = open(path+"/manifest.txt","r")
file=open(pathlist+"/lists/"+str(index)+".txt","a")
print(path)
path = sys.argv[1]

infile = open(path + "/manifest.txt", "r")
file = open(path + "/permissions.txt", "a")
contents = infile.read()
soup = BeautifulSoup(contents, 'xml')
titles = soup.find_all('uses-permission')
for title in titles:
    androidName = title.get('android:name');
    if androidName:
        file.write(androidName.split('.')[-1]+"\n")
    else:
        tagContent=title.string
        tagContent=tagContent.replace('\n','')
        tagContent=tagContent.replace('\t','')
        tagContent=tagContent.replace('>','')
        tagContent=tagContent.replace('=','')
        tagContent=tagContent.replace('"','')
        file.write(tagContent.split('.')[-1]+"\n")
<<<<<<< HEAD
=======
    file.write(title.get('android:name').split('.')[-1] + "\n")
>>>>>>> ede086ce26e6802da78452d0d5cf8e67bbf71cc4
