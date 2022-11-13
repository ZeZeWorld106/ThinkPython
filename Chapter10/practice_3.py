import time
def word_list1():
    t = []
    filename = 'words.txt'
    with open(filename) as f:
        for line in f:
            word = line.strip()
            t.append(word)
        return t

def word_list2():
    t = []
    filename = 'words.txt'
    with open(filename) as f:
        for line in f:
            word = line.strip()
            t += [word]
        return t

start_time = time.time()
diff = time.time() - start_time
