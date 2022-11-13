def newton_method():
    a = input('请输a:')
    x = input('请输b:')
    while True:
        print(x)
        y = (x+a/x)/2
        if y == x:
            break
        x = y