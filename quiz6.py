#Claire Yegian
#12/13/17
#quiz6.py 

dictionary = open('engmix.txt')

"""
#Program 1
list = []
for word in dictionary:
    if word.count('c') == 3 and word.count('p') == 2:
        list.append(word)
for word in list:
    word.strip()
    print(word)"""

"""
#Program 2
rList = []
for word in dictionary:
    if word != '':
        if word[0] == 'r':
            rList.append(word)
print(len(rList))"""

#Program 3
num = int(input('Enter a number: '))
for word in dictionary:
    word = word.strip()
    if len(word) == num:
        print(word)
        break

#Program 4
letter = input('Enter a letter: ')
noLetter= []
for word in dictionary:
    if word.count(letter) == 0:
        noLetter.append(word)
print(len(noLetter))