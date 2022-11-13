def print_n(s,n):
    while n > 0:
        print(s)
        n = n - 1
    print('Blastoff!')

print_n('Hello, world!',10)

x = int(input('请输入一个x:'))
a = int(input('请输入一个a:'))
while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y