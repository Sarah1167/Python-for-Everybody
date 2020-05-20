import re
fname=input('Enter a File to process: ')
fhand=open('mbox.txt')
regex=input('Enter a regular expression: ')

count=0
for line in fhand:
    line = line.rstrip()
    if re.findall(regex, line):
        count=count+1
print(fname, 'had', count, 'lines the matched', regex)
