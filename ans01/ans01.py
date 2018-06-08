#URL: http://www.pythonchallenge.com/pc/def/map.html

from string import maketrans


def main():
    phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    alphabetORIG = string.ascii_lowercase*2


    alphabetNEW = ''.join(alphabetORIG)

    alphabetORIG = alphabetORIG[:26]
    alphabetNEW = alphabetNEW[2:28]


    #print(alphabetORIG)
    #print(alphabetNEW)

    rosettaStone = string.maketrans(alphabetORIG,alphabetNEW)

    phrase.translate(rosettaStone)



'''
    for word in phrase:
        for ch in word:
            if ch.isalnum():
                #tmpValue = ord(ch) + 2
                aList.append(chr(ord(ch)+2))
            else:
                aList.append(ch)

    for word in aList:
        print(aList, end='')
'''

'''
def main2():

    phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    
    #phrase = "map"

    alphabet = list(string.ascii_lowercase)*2

    print()

    for word in phrase:
        for ch in word:
            if ch in alphabet:
                index = alphabet.index(ch)
                print(alphabet[index+2],end="")
            else:
                print(ch,end='')
    print()

'''
main()
