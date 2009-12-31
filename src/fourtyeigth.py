def powerself(num):
    return num**num
def sumf(num):
    sum=0
    for i in xrange(1,num+1):
        sum=sum+powerself(i)
    print str(sum)[-10:]

sumf(1000)