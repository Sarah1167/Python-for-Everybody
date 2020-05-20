import string
fhand=open('mbox-short.txt')

letters={}
for all in fhand:
    all=all.translate(str.maketrans('', '', string.punctuation))
    all=all.translate(str.maketrans('', '', ' '))
    all=all.rstrip()
    all=all.lower()
    for ch in all:
        letters[ch]=letters.get(ch, 0)+1

lecount=list()

for key, val in list(letters.items()):
    lecount.append((val, key))

lecount.sort(reverse=True)

for key, val in lecount:
    print(key, val)
