#Claire Yegian
#12/7/17
#longShort.py - prints shortest and longest words for each letter of alphabet

dictionary = open('engmix.txt')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

longest =['']*26
shortest = ['']*26
alphabetNum = 0
for word in dictionary:
    word = word.strip()
    if word != '':
        letter = alphabet[alphabetNum]
        letterList = []
        while word[0] == letter:
            letterList.append(word)
            longestWord = 0
            longestword = ''
            for line in letterList:
                if len(line)>=longestWord:
                    longestWord = len(line)
                    longestword = line
                longest[alphabetNum] = longestword
            shortestWord = longestWord
            shortestword = ''
            for line in letterList:
                if len(line)<=shortestWord:
                    shortestWord = len(line)
                    shortestword = line
                shortest[alphabetNum] = line
        alphabetNum = alphabetNum + 1