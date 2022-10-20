#practice 3-3
#这题不太容易，浅记一下一些经验
def row_element():
    '''定义行元素形态'''
    '''根据提示，print()末尾可以加上参数
    使得下一行的打印效果，可以跟上一行同行'''
    print("+ - - - -", end = " ")

def column_element():
    '''定义列元素，原理同上'''
    print("|        ", end = " ")

def do_twice(f):
    '''写一个函数用来翻倍调用次数：2倍 —— 针对行元素翻倍'''
    f()
    f()

def do_four(f):
    '''写一个函数用来翻倍调用次数：4倍 —— 针对列元素翻倍'''
    do_twice(f)
    do_twice(f)

def times_rows():
    '''定义该函数使得行可以翻倍'''
    do_twice(row_element)  #行元素*2，但是没有堵头
    print("+")  #所以在这，来个堵头

def times_columns():
    '''定义该函数使得列可以翻倍'''
    do_twice(column_element) #列元素*2，完成第二行建构
    print("|") #来一个堵头

def row_formation():
    '''定义一个函数，从行角度，组成元素'''
    times_rows()
    do_four(times_columns)

def formation():
    '''定义一个函数，对于行进行翻倍'''
    do_twice(row_formation)
    times_rows()  #封口

formation()

#4行4列
def row_element():
    print("+ - - - -", end = " ")

def column_element():
    print("|        ", end = " ")

def double(f):
    f()
    f()

def fourfold(f):
    double(f)
    double(f)

def times_rows():
    fourfold(row_element)
    print("+")

def times_columns():
    fourfold(column_element)
    print("|")

def row_formation():
    times_rows()
    fourfold(times_columns)

def formation():
    fourfold(row_formation)
    times_rows()

formation()