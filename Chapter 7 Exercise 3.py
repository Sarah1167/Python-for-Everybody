fname=input('Enter file name to find # of "Subject" lines: ')
if fname=='':
    fname='mbox.txt'
if fname=='na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been cock slapped')
    exit()
try:
    hand=open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count=0
for line in hand:
    if line.startswith('Subject'):
        count=count+1
print('There were', count, 'subject lines in', fname)
