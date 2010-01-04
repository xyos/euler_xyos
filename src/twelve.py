from seven import prime 
from twenty import factorial
def triangle_num(max_div):
    i=0
    num=0
    div=0
    while True:
       i=i+1
       num = num +i
def factors(num):
    prim=2
    lista=[]
    
    while num!=1:
        if num%prim==0:
            num=num/prim
            lista.append(prim)
        else:
            prim=next_prime(prim)
    print lista
    
def next_prime(prim):
    while True:
        prim=prim+1
        if prime(prim):
            return prim
factors(24)
