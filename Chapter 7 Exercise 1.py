fname=open('mbox-short.txt')
count=-1
for line in fname:
    count=count+1
    upper=line.upper()
    if count==5:
        break
    print(upper.rstrip())
