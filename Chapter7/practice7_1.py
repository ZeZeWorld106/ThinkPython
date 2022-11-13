import math
def square_root(a,x):
    '''接收一个a,及他的平方根'''
    '''同时使用合适的x逼近'''
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

def test_square_root(a,x):
    print('a\tmysqrt(a)\tmath.sqrt(a)\tdiff')
    print('-\t---------\t------------\t----')
    while a<10:
        print(a)
        result = square_root(a,x)
        confirm = math.sqrt(a)
        diff = result - confirm
        print(f'{a}\t{result}\t{confirm}\t{diff}')
        a -= 1
        if a==0:
            break

test_square_root(9,2)