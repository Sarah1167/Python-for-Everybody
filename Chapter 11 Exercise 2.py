import re
fname=input('Enter a File to process: ')
if fname=='1':
    fname='mbox.txt'
if fname=='2':
    fname='mbox-short.txt'

try:
    fhand=open(fname)
except:
    print('FILE NOT FOUND')
    exit()

numlist=list()
for line in fhand:
    line=line.rstrip()
    num=re.findall('^New .* ([0-9]+)', line)
    if len(num)>0:
        for number in num:
            number = int(number)
            numlist.append(number)

print(sum(numlist)//len(numlist))
