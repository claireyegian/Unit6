dictionary = open('engmix.txt')

word2 = input('Enter a word: ')
x = ''
for word in dictionary:
    if word==word2:
        x = word
print(x)