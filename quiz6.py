#Claire Yegian
#12/13/17
#quiz6.py 

dictionary = open('engmix.txt')

#Program 1
cList = []
pList = []
for word in dictionary:
    if word.count('c') == 3:
        cList.append(word)
    if word.count('p') == 2:
        pList.append(word)
print(cList,'all have 3 cs')
print(pList,'all have 2 ps')
    

