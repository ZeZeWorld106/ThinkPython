numbers = [42, 123]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

#列表中最为重要的三种运算,reduce运算
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

t = [1, 2, 3]
total = add_all(t)
print(total)
print(sum(t))

#将运算应用到一个序列中的每个元素上，map()
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())

    return res

z = ['liu','yao','ze']
print(capitalize_all(z))

#筛选出特定的元素，过滤掉其他的，filter()
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

#加索引的删除：pop()【没有的话就是最后一个元素】,
t = ['a','b','c']
x = t.pop(1)
print(t)
#不需要删除的值了
t = ['a','b','c']
del t[1]
print(t)
#知道元素不知道位置，remove（），返回值是空
t = ['a','b','c']
t.remove('b')
print(t)
#删除更多元素
t = ['a','b','c','d','e','f']
del t[1:5]
print(t)

#字符串可以直接转换成字母分离的列表
s = 'spam'
t = list(s)
print(t)

#使用split（）和join（）
s = 'spam-spam-spam'
#split()用的是，字符串.方法()
delimiter = '-'
s = s.split(delimiter)
print(s)

t = ['pining','for','the','fjords']
#join()用的是，符号.方法()
delimiter = ' '
s = delimiter.join(t)
print(s)

#字符串一个对象，列表两个对象
#但是一个重要的点：
#如果两个对象是同一个对象，那么他们必然想等
#但是如果他们想等，未必是一个对象
#别名是可以的，但是对于可变对象，避免别名的使用
def delete_head(t):
    del t[0]
    
letters = ['a','b','c']
delete_head(letters)
print(letters)

#要改变原列表的话，使用append()，如果不需要的话，使用+号

def tail(t):
    return t[1:]

letters = ['a','b','c']
rest = tail(letters)
print(rest)


