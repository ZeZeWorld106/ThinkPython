def  ack(m,n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1,ack(m, n-1))

print(ack(3,4))
#递归超出限制
#print(ack(1000, 1200))