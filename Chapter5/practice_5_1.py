#practice 5_1
'''import time
t = time.time()

def counting_time():
    seconds = int(t)
    minutes = t // 60
    hours = minutes // 60
    days = hours // 24
    print(f"从纪元到现在一共约有{days}天")
    print(f"一共约有{hours}小时")
    print(f"一共约有{minutes}分钟")
    print(f"一共约有{seconds}秒")

counting_time()'''

#practice 5_2
a = int(input())
b = int(input())
c = int(input())
n = int(input())

def check_fermat(a,b,c,n):
    
    if n > 2 and (a**n + b**n == c**n):
        print("天呐，费马弄错了！")
    else:
        print("不，那样不行！")

check_fermat(a, b ,c , n)

#practice 5_3
a = int(input())
b = int(input())
c = int(input())

def is_triangle(a,b,c):
    if a+b > c or a+c > b or b+c > a:
        print("Yes，能够组成三角形")
    elif a+b == c or a+c == b or b+c == a:
        print("Yes，能够组成三角形")
    else:
        print("No，不能组成三角形")
    
is_triangle(a, b, c)

#practice5_4
#【迭代】
def recurse(n,s):
    '''这是一个递归的函数，主要是用于调用自己来达到循环的目的'''
    '''过程为：n=3,s=0;n=2,s=3;n=1,s=5;n=0,s=6'''
    '''最终的输出为6'''
    if n == 0:
        print(s)
    else:
        recurse(n-1,n+s)

recurse(3, 0)
recurse(-1, 0) #最大的递归层次已经到了

#practice 5_5
import turtle
def draw(t, length, n):
    t = turtle.Turtle()
    print(t)
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

    turtle.done()
draw('bob',20,20)

import turtle
def koch_curve(t, x):
    t = turtle.Turtle()
    print(t)

    if x < 10:
        t.fd(x)
        return
    q = x/3
    t.lt(60)
    t.fd(q)
    t.rt(120)
    t.fd(q)
    t.lt(60)
    t.fd(q)


def snowflake(t,x):
    for i in range(3):
        koch_curve(t, x)
        t.rt(120)
    
snowflake('bob',300)
