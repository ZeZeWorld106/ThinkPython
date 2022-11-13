def eval_loop():
    while True:
        string = input('请输入:')
        if string == 'done':
            break
        else:
            result = eval(string)
            print(result)
    print(result)

eval_loop()