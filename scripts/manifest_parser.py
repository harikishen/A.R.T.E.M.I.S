from bs4 import BeautifulSoup
import sys

path=sys.argv[1]

infile = open(path+"/manifest.txt","r")
file=open(path+"/permissions.txt","a")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
titles = soup.find_all('uses-permission')
for title in titles:
    file.write(title.get('android:name').split('.')[-1]+"\n")