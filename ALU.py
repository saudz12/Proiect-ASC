import numpy as np

def complement(a):
    i=len(a)-1
    while i>=0:
        if(a[i]==1):
            i-=1
            break
        i-=1
    while(i>=0):
        if(a[i]==1):
            a[i]=0
        else:
            a[i]=1
        i-=1
    return a
        

def negat(a):
    i=len(a)-1
    while i>=0:
        if(a[i]==1):
            a[i]=0
        else:
            a[i]=1
        i-=1
    return a

def ADD(a,b):
    t=0
    r=[]
    for i in range(0,len(a)):
        r+=[0]
    
    i,j= len(a)-1,len(b)-1
    while i>=0 or j>=0 or t:
        total=t
        if i>=0:
            total+=a[i]
            i-=1
        if j>=0:
            total+=b[i]
            j-=1   
        r[i]+=total%2
        t=total//2
    return r    

def AND(a,b):
    for i in range(0,len(a)):
        a[i]=a[i] and b[i]
    return a

def OR(a,b):
    for i in range(0,len(a)):
        a[i]=a[i] or b[i]
    return a
     
def XOR(a,b):
    for i in range(0,len(a)):
        a[i]=(a[i]+b[i])%2
    return a

def SUBTR(a,b):
    t=0
    r=[]
    for i in range(0,len(a)):
        r+=[0]
    for i in range(0,len(a)):
        if t:
            a[i]-=1
        suma=a[i]-b[i]
        if suma<0:
            t=1
            suma+=2
        else: 
            t=0
        r[i]+=suma%2
    return r

def INCR(a):
    return ADD(a,1)
def DECR(a):
    return SUBTR(a,1)

def MULTIPLY(m,r):
    a=[]
    s=[]
    p=[]
    for i in range(0, 10):
        a+=[0]
        s+=[0]
        p+=[0]
        
    for i in range(0,len(m)-1):
        if i==0:
            a[i]=1
        else:
            a[i]=m[i]
            
    for i in range(0,len(m)-1):
        if i==0:
            s[i]=0
        else:
            s[i]=m[i]
            
    for i in range(0,10):
            p[i]=0
    

    
    return p


def DIVIDE(a,b):
    return

def SHIFT_R():
    return
def SHIFT_L():
    return
def ALU(a,b,opr):
    match opr: 
        case [0,0,0,0,0]: 
                return a
        case [0,0,0,0,1]:
                return b
        case [0,0,0,1,0]:
                return complement(a) #functie pt a complementar
        case [0,0,0,1,1]:
                return complement(b) #functie pentru b complementar
        case [0,0,1,0,0]:
                return negat(a) #functie pentru !a
        case [0,0,1,0,1]:
                return negat(b) #functie pentru !b    
        case [0,0,1,1,0]:
                return OR(a,b)
        case [0,0,1,1,1]:
                return AND(a,b)
        case [0,1,0,0,0]:
                return ADD(a,b) #functie ADD with carry 
        case [0,1,0,0,1]:
                return SUBTR(a,b) #scadere cu transport
        case [0,1,0,1,0]: 
                return XOR(a,b) #functie XOR a,b 
        case [0,1,0,1,1]:
                return INCR(a)
        case [0,1,1,0,0]:
                return INCR(b)
        case [0,1,1,0,1]:
                return DECR(a)
        case [0,1,1,1,0]:
                return DECR(b)
        case [0,1,1,1,1]:
                return MULTIPLY(a,b)
        case [1,0,0,0,0]:
                return DIVIDE(a,b)
        case [1,0,0,0,1]:
                return SHIFT_R(a)
        case [1,0,0,1,0]:
                return SHIFT_L(a)
        case [1,0,0,1,1]:
                return
        case [1,0,1,0,0]:
                return
        case [1,0,1,0,1]:
                return
        case [1,0,1,1,1]:
                return
        
print(ALU([1,0,0,0],[1,0],[0,1,1,1,1]))
