filename = 'words.txt'
with open('words.txt') as f:
    sheet = f.read()

def pair(sheet):
    for word in sheet:
        j = 0
        count = 0
        while j < len(word)-1:
            if word[j] == word[j+1]:
                count += 1
                if count == 3:
                    print(word)
                j += 2
            else:
                count = 0
                j += 1
pair(sheet)
