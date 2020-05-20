#Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are.
fname=input('Enter a txt File name, that you want to enter all the words into a Python Dictionary: ')
if fname=='1':
    fname='words.txt'
try:
    fhand=open(fname, 'r')
except:
    print('FILE NOT FOUND')

dwords={}
k=list()
for line in fhand:
    word = line.split()
    k=k+word

le=len(k)
count=0
x=0

while le>count:
    a=k[x]
    dwords.update({a:None})
    count=count+1
    x=x+1

print(dwords)
print('Gubba nub nub doo rah kah')
