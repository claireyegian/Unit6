#Claire Yegian
#12/13/17
#quiz6.py 

dictionary = open('engmix.txt')

#Program 1
cList = []
pList = []
for word in dictionary:
    word.split()
    if word.count('c') == 3:
        cList.append(word)
    if word.count('p') == 2:
        pList.append(word)
for word in cList:
    print(word+'has 3 cs')
for word in pList:
    print(word+'has 2 ps')
    

