fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if line.startswith('From ') and len(words)>2:
        print(words[2])
