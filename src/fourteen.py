def collatz(num):
    counter = 1
    while True:
        if num == 1:
            return counter
        if num%2==0:
            num = num/2
            counter=counter+1
        else:
            num = 3*num+1
            counter=counter+1
def fourteen(num):
    max=0
    val=0
    for i in xrange(1,num):
        temp=collatz(i)
        if temp>max:
            val=i
            max=collatz(i)
    return val, max
print collatz(837799)
    


