import math
def area(radius):
    a = math.pi * radius**2
    return a


'''def area(radius):
    return math.pi * radius**2'''


'''def absolute_value(x):
    #每一个可能的执行路径都需要可以遇到return语句才可以
    #这个例子中的x = 0就不可以用
    if x > 0:
        return x
    if x < 0:
        return -x
print(absolute_value(10))'''

#课中例题1
'''def compare(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    else:
        return -1

print(compare(1,4))'''

#增量开发
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    #print('dx is',dx)
    #print('dy is',dy)
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    #print('dsquared is', dsquared)
    return result

print(distance(1, 2, 4, 6))

#课中习题2
"""def hypotenuse(x, y):
    '''给定直角三角形的两边可以得到第三边'''
    l1 = x
    l2 = y
    l3_squared = l1**2 + l2**2
    l3 = math.sqrt(l3_squared)
    #print(l1)
    #print(l2)
    #print(l3)
    return l3

print(hypotenuse(3,4))"""

#组合（函数调用函数，把函数封装起来）
#使用组合来简化函数
'''def circle_area(xc,yc,xp,yp):
    #radius和result的临时变量在调试的时候是有用的，但是可以简写
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

print(circle_area(1, 4 ,5, 7))'''

#布尔函数，用来隐藏函数内复杂的检测
'''def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False

print(is_divisible(6,4))'''

##布尔函数的特殊性是（用‘==’）
"""def is_divisible(x,y):
    return x % y == 0

'''print(is_divisible(6,4))'''

##布尔函数常常用于条件语句中，就没有返回值了
if is_divisible(6,4):
    print("x is divisible by y")

#课中习题3
def is_between(x,y,z):
    if x<=y<=z:
        return x<=y<=z
    else:
        return False

'''if is_between(8,3,4):
    print("条件成立~")'''

print(is_between(8,3,4))

#再看递归
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

#控制类型输入
def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers")
        return None
    elif n<0:
        print("Factorial is not defined for negative integers.")
        return None
    elif n == 0:
        return 1 
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial('fred'))
print(factorial(-1))"""

def factorial(n):
    space = ' ' * (4*n)
    print(space,'factrorial',n)
    if n ==0 :
        print(space, "returning 1")
        return 1
    else:
        recurse = factorial(n-1)
        result = n*recurse
        print(space,'returning',result)
        return result

print(factorial(4))