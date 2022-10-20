#practice 3_2
#1.输入例子
def do_twice(f):
    '''定义一个执行两次函数的操作'''
    '''f虽为名称名称形式，但是在函数体内加了（）,代表操作'''
    f()
    f()
 
def print_spam():
    print('spam')
    
do_twice(print_spam)

#2.接收两个实参，一个函数对象，一个值
def do_twice(f, a):
    f(a)
    f(a)
def print_spam(a):
    print(a)

do_twice(print_spam, "Hello, world!")

#3. 添加函数的定义
def do_twice(f, a):
    f(a)
    f(a)
    
def print_twice(content):
    '''这个函数在调用时会把实参的值赋到形参 f上，将其打印两次'''
    print(content)
    print(content)
#4. 使用修改版的do_twice调用print_twice两次，并传入实参'spam'
def do_twice(f, a):
    f(a)
    f(a)
    
def print_twice(content):
    '''这个函数在调用时会把实参的值赋到形参 f上，将其打印两次'''
    print(content)
    print(content)
    
do_twice(print_twice,'spam')
#4. 定义一个函数，do_four
###这一题不是说题目要求的，但是在这里练习一下书里面讲的，表达式改变
def do_four(f, a):
    f(a*2)
    f(a*2)

def print_twice(content):
    print(content)
    print(content)
    
do_four(print_twice, "Hello, World!")

###真正的题目在这里
def do_twice(f, a):
    f(a)
    f(a)

def do_four(f , a):
    do_twice(f, a)
    do_twice(f, a)
    
def print_one_time(a):
    print(a)
    
    
do_four(print_one_time,'Hello, World!')


