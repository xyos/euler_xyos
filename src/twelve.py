from seven import prime 
from twenty import factorial
def triangle_num(max_div):
    i=0
    num=0
    div=0
    val=0
    while max_div>div:
       i=i+1
       num = num +i
       temp=factors(num)
       if div<temp:
        div=temp
        val=num
        print val
        print div
    return val

def factors(num):
    prim=2
    lista=[]
    
    while num!=1:
        if num%prim==0:
            num=num/prim
            lista.append(prim)
        else:
            prim=next_prime(prim)
    current = 0
    factors = 1
    for i in lista:
        if i !=current:
            factors = factors*(lista.count(i)+1)
            current = i
    return factors
    
def next_prime(prim):
    while True:
        prim=prim+1
        if prime(prim):
            return prim
print triangle_num(500)