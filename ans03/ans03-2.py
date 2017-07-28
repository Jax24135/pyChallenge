# HINT: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

## Trial method
## Find lowercase letters
## save index location
## cut substring by +/- 3 with the center LOWERCASE letter
## run outer SUBSTRING through an UPPERCASE test // keeping LOWECASE out
## if still true >> add to LIST

## Go to next LOWERCASE letter

import string

def bodyguard_check(center,ctr_char,substring):
    flag = "TRUE"
    i = 0

    while flag == "TRUE" and i < len(substring):
        if i != 3:
            if substring[i].isupper():
                i += 1
            else:
                flag = "False"
                
        elif i == 3:
            if substring[i].islower():
                i += 1
        else:
            flag = "False"

    # After TESTING        
    if flag == "TRUE":
        return ctr_char

def verify_slice(center,phrase):
    if center >= 3:
        start = center - 3
    else:
        start = 0
    if center < (len(phrase) - 4):
        end = center + 4
    else:
        end = len(phrase)
    return start,end
    


def main():
    inFile1 = open('gibberish.dat','r')
    outFile = open('tmp.dat','w')
    #phrase = "kAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbT" 
    #phrase = "KAEWTLoYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbT" 
    #phrase = 'aAAcBBBdEEE'
    filtered=[]


    for line in inFile1:
        line = line.strip()
        outFile.write(line)

    outFile.close()
    inFile2 = open('tmp.dat','r')
    phrase = inFile2.read()
    
    #for phrase in inFile:
    for ch in phrase:
        if ch.islower():
            center = phrase.index(ch)
            start, end = verify_slice(center,phrase)
            substring = phrase[start:end]
            tmp = bodyguard_check(center,ch,substring)
            if tmp != None:
                filtered.append(tmp)
            #print(filtered,end='')
            
    #print(center,substring)
    #combine = ''.join(filtered)
    print(filtered)
    print('done')

main()
