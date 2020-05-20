fname=input('Enter file name: ')
if fname=='s':
    fname="mbox-short.txt"
if fname=='l':
    fname="mbox.txt"
try:
    fhandle=open(fname)
except:
    print(fname, 'FILE NOT FOUND')
    exit()
count=0
conf=0.0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:',):
        line=line[19:].rstrip()
        count=count+1
        conf=conf+float(line)
        avg=conf/count
print('The average confidence is:', avg)
