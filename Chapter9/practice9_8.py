def is_num():
    for i in range(100000, 1000000):
        if str(i)[2:] == str(i)[:1:-1]:
            i += 1
            if str(i)[1:] == str(i)[5:0:-1]:
                i += 1
                if str(i)[1:-1] == str(i)[-2:0:-1]:
                    i += 1
                    if str(i) == str(i)[::-1]:
                        c = i-3
                        print(c)