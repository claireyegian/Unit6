#Claire Yegian
#12/7/17
#palindromes.py - prints all palindromes in dictionary

dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip()
    wordList = list(word)
    wordList.reverse()
    wordReverse = ''
    for ch in wordList:
        wordReverse = (wordReverse+ch)
    if word == wordReverse:
        print(word)
