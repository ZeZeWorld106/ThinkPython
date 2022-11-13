'''def nested_sum(t):
    total = 0
    for i in t:
        total += sum(i)
    return total 

t = [[1, 2], [3], [4, 5, 6]]
z = nested_sum(t)

print(z)'''

def cumsum(t):
    count = 0
    result = []
    for i in t:
        count += i
        result.append(count)
    return result

def middle(t):
    return t[1:-1]

t = [1, 2, 3, 4]
print(middle(t))

def chop(t):
    del t[0], t[-1]

def is_sorted(t):
    if t == sorted(t):
        return True
    else:
        return False
print(is_sorted(t))

def is_anagram(string_1, string_2):
    if sorted(string_1) == sorted(string_2):
        return True
    else:
        return False
print(is_anagram('dad','dad'))

def has_duplicates(s):
    t = list(t)
    z = t.sort()

    for i  in range(len(z)-1):
        if t[i] == t[i+1]:
            return True

    return False

