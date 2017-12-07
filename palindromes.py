#Claire Yegian
#12/7/17
#palindromes.py - prints all palindromes in dictionary

dictionary = open('engmix.txt')

for word in dictionary:
    wordList = list(word)
    wordReverse = ''
    for ch in wordList:
        wordReverse = wordReverse + ch
    if word == wordList.reverse:
        print('yay')
