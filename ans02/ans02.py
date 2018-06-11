#URL: http://www.pythonchallenge.com/pc/def/ocr.html

def main2():

    inFile = open('gibberish.txt','r')

    for line in inFile:
        for ch in line:
            if ch.isalnum():
                print(ch,end='')


'''
def main():

    inFile = open('gibberish.txt','r')

    for line in inFile:
        for ch in line:
            if ch.isalpha():
                print(ch,end='')
'''
main2()
