def main():
    inFile = open('gibberish.txt','r')

    for line in inFile:
        for ch in line:
            if ch.isalpha():
                print(ch,end='')

main()
