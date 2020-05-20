fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From '):
        words = line.split()
    if len(words)>2:
        print(words[2])
