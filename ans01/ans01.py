#URL: http://www.pythonchallenge.com/pc/def/map.html

import string


def main():
    phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    alphabet = list(string.ascii_lowercase)*2

    aList = []

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
def main2():

    phrase = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
    
    phrase = "map"

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
