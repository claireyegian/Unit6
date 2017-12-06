#Claire Yegian
#12/6/17
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    if 'claire' in word:
        print(word.strip())
    wordCount += 1

print('There are', wordCount,'words in the dictionary.')