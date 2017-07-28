# HINT: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import string

# define UPPERCASE alphabet
# if UPPERCASE is found, text next index
# if UPPERCASE still found, text next index
# if UPPERCASE is found...yet again --print next character

def bodyguard_check(start,phrase):                                                             
    # use the starting index of the first UPPERCASE letter
    # slice the next 7 characters 
    FLAG = "TRUE"
    i = 0
    search = phrase[start:(start+7)]
    print(search)

    while FLAG == "TRUE" and i < len(search):
        if i != 3:
            if search[i].isupper():
                eos = search[i]
                i += 1
                special = ''
            
        elif search[3].islower():
            special=search[3]
            eos = search[i]
            i += 1
            
        else:
            special=''
            eos = search[i]
            FLAG = "FALSE"
    return special, eos


                                                                                   
def main():                                                                           
    #inFile = open('gibberish.dat','r')                                             
                                                                                                
    phrase = "kAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbT" 
    phrase = 'AAAcBBB'
   # u_alpha = list(string.ascii_uppercase)
    filtered=[]
    
    for ch in phrase:
        if ch.isupper():
            start = phrase.index(ch)
            special, eos = bodyguard_check(start,phrase)
            filtered.append(bodyspecial)
        ch = phrase.find(eos)
    print(filtered)

main()
