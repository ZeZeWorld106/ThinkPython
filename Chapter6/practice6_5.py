#6-5
def gcd(a,b):
    if a<b:
        a,b = b,a
    r = a % b
    while r != 0:
        gcd(b,r)
gcd(1,3)