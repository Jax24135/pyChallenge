#URL: http://www.pythonchallenge.com/pc/def/map.html

import string


def main():

    #import URL phrase to translate
    #phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    phrase = "map"

    #create a LIST based on the alphabet (x2 to catch first two letters on repeat)
    alphaORIG = string.ascii_lowercase*2

    #make a STRING out of a LIST
    alphaNEW = ''.join(alphaORIG)


    #cut variables to 26 letters so mapping works
    # alphaNEW is 2 letters ahead of alphaORIG (a >> c, b >> d)
    alphaORIG = alphaORIG[:26]
    alphaNEW = alphaNEW[2:28]


    #DEBUG --confirm it works
    #print(alphaORIG)
    #print(alphaNEW)


    #use MAKETRANS to create mapped translation object
    rosaStone = str.maketrans(alphaORIG,alphaNEW)

    #use rosettaStone (ie rosaStone) to print decyphered text
    print(phrase.translate(rosaStone))

main()
