import random

def has_same_bd(t):
    z = t[:]
    z.sort()

    for i in range(len(z)-1):
        if z[i] == z[i+1]:
            return True
    else:
        return False

def ran_bd(n):
    res = []
    for i in range(n):
        bd = random.randint(1,365)
        res.append(bd)
    return res

def count_same(student_n, same_n):
    for i in range(same_n):
        t = ran_bd(student_n)
        if has_same_bd(t):
            count += 1
    return count