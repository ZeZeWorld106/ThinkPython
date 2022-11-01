#6-4
import math
def is_power(a, b):
    a = b**2
    b = math.sqrt(a)
    if b == 0:
        return False
    if a == b**2 and a/b == b**2 and a%b ==0:
        return True
    else:
        return False