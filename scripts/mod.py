file = open("FINAL_LIST")
listfile = open("WATCH_LIST","a+")

text = file.read().split("\n")
for eachone in text:
	eachone = eachone.split(" ")
	listfile.write(eachone[0]+"\n")
print(text)