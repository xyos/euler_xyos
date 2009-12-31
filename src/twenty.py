def factorial(num):
    fact=1
    for i in xrange(1,num+1):
        fact=fact*i
    return fact
cadena = str(factorial(100))
sum=0
for i in cadena:
    print i
    sum = sum+int(i)
print sum


