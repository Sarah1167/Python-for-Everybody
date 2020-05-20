fname=input('Enter file name: ')
if fname=='1':
    fname='mbox-short.txt'
try:
    fhand=open(fname, 'r')
except:
    print('FILE NOT FOUND')
    exit()

days={}

for line in fhand:
    if not line.startswith('From '):
        continue
    line=line.rstrip()
    words=line.split()
    d=words[2]
    if d not in days:
        days[d]=1
    else:
        days[d]+=1

print(days)
