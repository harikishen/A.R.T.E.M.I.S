from bs4 import BeautifulSoup
import sys


def manifest_parse(filePath):
    permissions = []
    path = filePath
    pathlist = path.split("/")
    index = pathlist.pop()
    print(" list ::: ", pathlist)
    pathlist = "/".join(pathlist)
    infile = open(path + "/manifest.txt", "r")
    contents = infile.read()
    soup = BeautifulSoup(contents, 'xml')
    titles = soup.find_all('uses-permission')
    for title in titles:
        androidName = title.get('android:name')
        if androidName:
            permissions.append(androidName.split('.')[-1])
        else:
            tagContent = title.string
            tagContent = tagContent.replace('\n', '')
            tagContent = tagContent.replace('\t', '')
            tagContent = tagContent.replace('>', '')
            tagContent = tagContent.replace('=', '')
            tagContent = tagContent.replace('"', '')
            permissions.append(tagContent.split('.')[-1])
    return permissions
