#URL http://www.pythonchallenge.com/pc/def/equality.html

import re, urllib.request

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

result = re.findall("""[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]""", data)
result = ''.join(result)

#inFile = open("clean.dat",'r')


#line = inFile.read()
#line = "aDDDzBBBc"

print("\nAnswer is ")
print(result)


















#print("".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", line)))