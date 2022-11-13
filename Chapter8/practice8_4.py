def get_word(a, fron, back):
    while a > back:
        a -= 26
    while a < fron:
        a += 26
    return a 

def rotate_word(word, num):
    new = ''
    for i in word:
        if i.isupper():
            new += chr(get_word(ord(i) + num,65,90))
        elif not i.isalpha():
            new += i
        else:
            new += chr(get_word(ord(i) + num, 97, 122))
    return i

print(rotate_word('sdfasdfasdfadsfq3i4uhfuds',13))