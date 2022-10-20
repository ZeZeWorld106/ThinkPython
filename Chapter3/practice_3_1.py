#practice 3_1
def right_justify(s):
    '''定义一个最后一个字符显示在第70列的函数'''
    content = len(s)
    print(' '*(70-len(s)) + s)
    
right_justify('monty')
