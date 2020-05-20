#sets up varibles needed
k=list()
x=0
#open da file
fhand=open('romeo.txt')
#Pull lines of the file and split into words for list
for lines in fhand:
    j=lines.split()
    k=k+j
#sort the list
k.sort()
#count the amouth of words in file -1 for offset
z=len(k)-1
#count down, all the while
while z>0:
    z=z-1
    #if the values are not same skip
    if k[x]!=k[x+1]:
        x=x+1
    #if values are same delete the first
    elif k[x]==k[x+1]:
        del k[x]
#prints a list of all words sorted alphabetically with no repeating words in list
print(k)
