def fibt(num):
    len = 0
    fib = 1
    temp = 1
    temp1 = 1
    count = 2
    while num>fib:
        temp1 = fib
        fib = fib + temp
        temp = temp1
        count = count + 1
    print count, fib
    
fibt(10**999)
