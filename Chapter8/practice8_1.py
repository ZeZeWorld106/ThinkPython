filename = 'words.txt'
with open (filename) as f:
    for line in f:
        print(line.rstrip())

filename = 'words.txt'
with open (filename) as f:
    for line in f:
        print(line.replace('a','hhh'))
