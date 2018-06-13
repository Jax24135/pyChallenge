

inFile = open("gibberish.dat",'r')
outFile = open("clean.dat",'w')

for line in inFile:
    line = line.strip('\n')
    outFile.write(line)

inFile.close()
outFile.close()
