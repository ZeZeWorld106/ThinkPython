import math
def estimate_pi():
    k = 0
    formal_i = 1
    total = 0

    while formal_i >1e-15:
        formal_i = ((math.factorial(4.0*k))*(1103 + 26390 *k))\
        /(math.factorial(k)**4)*(396.0**(4.0*k))
        k += 1
        total += formal_i

    output = ((2* math.sqrt(2))/9801) * total
    return 1 / output

print(estimate_pi())
print(math.pi())

