#URL http://www.pythonchallenge.com/pc/def/equality.html

import re

inFile = open("clean.dat",'r')

result=''

for line in inFile:
    m = re.search(r"[A-Z]{3}[a-z][A-Z]{3}", line).group(0)
    m = m[3:4]
    result+=m
    m = ''


# [A-ZA-ZA-Za-zA-ZA-ZA-Z]