from bs4 import BeautifulSoup
import sys

path=sys.argv[1]
# path="/home/deon/apk/1/"
# filenames=glob.glob(path+"*.apk")
# for filename in filenames:
#     dir=filename.split('/')[-1].split('.')[0]
#     path1="%s/%s"%(path,dir)

infile = open(path+"/manifest.txt","r")
file=open(path+"/permissions.txt","a")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
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
