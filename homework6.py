dictionary = open('engmix.txt')

word2 = input('Enter a word: ')
x = ''
for word in dictionary:
    word = word.strip()
    if word==word2:
        x = word
if x!='':
    print('Your word is in the dictionary')
else:
    print('Your word is not in the dictionary')