filename = 'words.txt'
with open(filename) as f:
    sheet = f.read().split()

for word in sheet:
    if len(word) > 20:
        print(word)

def has_no_e(word):
    return word.find('e') == -1

length = len(sheet)
for word in sheet:
    if has_no_e(word):
        without_e = word
        percentage = float(len(without_e)) / length
        print(f"{percentage:.2%}")

word = str('sam')
string = str('ae')
def avoids(word, string):
    for i in string:
        if i in word:
            return False
    return True

print(avoids(word, string))

aim = 'hsoidfo'
def use_only(word, string):
    for i in word:
        if i not in string:
            return False
    return True

for word in sheet:
    if use_only(word,aim):
        words = print(word)

def is_abecedarian(word):
    return word == ''.join(sorted(word))
for word in sheet:
    if is_abecedarian(word):
        words = print(word)




