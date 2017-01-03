from bs4 import BeautifulSoup

infile = open("manifest.txt", "r")
contents = infile.read()
soup = BeautifulSoup(contents, 'xml')
titles = soup.find_all('uses-permission')
for title in titles:
    print(title.get('android:name').split('android.permission.')[1])
