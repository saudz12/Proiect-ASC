import numpy as np
from variables import emptyMux, emptyReg

def complement(bin_list):
    """Complement in baza 2"""
    inverted = [1 - bit for bit in bin_list]
    one = [0] * (len(bin_list) - 1) + [1]
    return ADD(inverted, one)
        

def negat(a):
    i=len(a)-1
    while i>=0:
        if(a[i]==1):
            a[i]=0
        else:
            a[i]=1
        i-=1
    return a

def ADD(bin1,bin2):
    """Adunare"""
    max_len = max(len(bin1), len(bin2))
    
    # asiguram ca ambele numere sunt reprezentate pe acelasi nr de biti
    while len(bin1) < max_len:
        bin1.insert(0, 0)
    while len(bin2) < max_len:
        bin2.insert(0, 0)
    
    result = []
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        total_sum = carry + bin1[i] + bin2[i]
        carry = total_sum // 2
        result.insert(0, total_sum % 2)
    
    return result[-max_len:]  # Taiem la lungimea initiala

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
    max_len = max(len(a), len(b))
    while len(a) < max_len:
        a.insert(0, 0)
    while len(b) < max_len:
        b.insert(0, 0)
    result = [0] * max_len
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        diff = a[i] - b[i] - borrow
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0
        result[i] = diff
    #Scoatem 0-urile in plus din fata
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result

def INCR(a):
    return ADD(a,1)
def DECR(a):
    return SUBTR(a,1)

def MULTIPLY(multiplicand, multiplier):
    """Alg. lui Booth"""
    n = len(multiplicand)

    A = multiplicand + [0] * (n + 1)
    S = complement(multiplicand) + [0] * (n + 1)
    P = [0] * n + multiplier + [0]
    #print(A)
    #print(S)
    #print(P)
    for i in range(n):
        if P[-2:] == [0, 1]:
            P = ADD(P, A)
            
        elif P[-2:] == [1, 0]:
            P = ADD(P, S)
        P =SHIFT_R(P)

    return P[:-1]
def GREATER_EQ(a,b):
    max_len = max(len(a), len(b))
    while len(a) < max_len:
        a.insert(0, 0)
    while len(b) < max_len:
        b.insert(0, 0)
    for x,y in zip(a,b):
        if x>y:
            return True
        elif x<y:
            return False
    return True
def DIVIDE(N,D):
    if all(d==0 for d in D):
        return [1]*len(N)
        
    R=[0]*(len(N)+1)
    Q=[0]*len(N)
    for i in range (len(N)):
        R=SHIFT_L(R)
        R[-1]=N[i]
        if(GREATER_EQ(R,D)):
            R=SUBTR(R,D)
            Q[i]=1
    return Q

def SHIFT_R(x):
    y=[0]*len(x)
    y[0]=x[0] 
    for i in range(1,len(x)):
          y[i]=x[i-1]
    return y

def SHIFT_L(x):
    y=[0]*len(x)
    y[len(x)-1]=x[len(x)-1] 
    for i in range(len(x)-2,0,-1) :
          y[i]=x[i+1]
    return y

def SHIFT_RC(x):
    y=x[len(x)-1]
    x=SHIFT_R(x)
    x[0]=y
    return x
    
def SHIFT_LC(x):
    y=x[0]
    x=SHIFT_L(x)
    x[len(x)-1]=y
    return x
def NAND(a,b):
    r = []
    for b1, b2 in zip(a, b):
        r.append(1 - (b1 & b2))

    return r
def NOR(a,b):
    r = []
    for b1, b2 in zip(a, b):
        r.append(1 - (b1 | b2))

    return r

def XNOR(a,b):
    r =[]
    for b1,b2 in zip(a,b):
        r.append(1 if b1==b2 else 0)
    return r
def ALU(a,b,opr):
    match opr: 
        case [0,0,0,0,0]: 
                return b
        case [0,0,0,0,1]:
                return negat(a)
        case [0,0,0,1,0]:
                return complement(a) 
        case [0,0,0,1,1]:
                return INCR(a) 
        case [0,0,1,0,0]:
                return DECR(a) 
        case [0,0,1,0,1]:
                return OR(a, b)    
        case [0,0,1,1,0]:
                return AND(a,b)
        case [0,0,1,1,1]:
                return ADD(a,b)
        case [0,1,0,0,0]:
                return SUBTR(a,b) 
        case [0,1,0,0,1]:
                return MULTIPLY(a,b) 
        case [0,1,0,1,0]: 
                return DIVIDE(a,b) 
        case [0,1,0,1,1]:
                return XOR(a, b)
        case [0,1,1,0,0]:
                return SHIFT_R(a)
        case [0,1,1,0,1]:
                return SHIFT_L(a)
        case [0,1,1,1,0]:
                return SHIFT_RC(a)
        case [0,1,1,1,1]:
                return SHIFT_LC(a)
        case [1,0,0,0,0]:
                return NOR(a, b)
        case [1,0,0,0,1]:
                return NAND(a, b)
        case [1,0,0,1,0]:
                return XNOR(a, b)
        case [1,0,0,1,1]:
                return SHIFT_RC(a)
        case [1,0,1,0,0]:
                return SHIFT_LC(a)
        case [1,0,1,0,1]:
                return NAND(a,b)
        case [1,0,1,1,0]:
                return NOR(a,b)
        case [1,0,1,1,1]:
                return XNOR(a,b)
        case [1,1,1,0,1]:
                return list(emptyReg)
        case [1,1,1,1,0]:
                return b 
        case [1,1,1,1,1]: 
                return a 
        
#print(ALU([1,0,1,1],[1,1,0,1],[1,0,1,1,1]))
