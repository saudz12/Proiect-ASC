import numpy as np

BYTESCOUNT = 1
REGISCOUNT = 15

cuvantControl = []

sela = []
selb = []
seld = []
opr = []

arr = []

output = []
#print(registers)

  

def initializeRegisters():
    global arr
    for i in range(0, REGISCOUNT+1): #number of registers - depends on number of bits in SELD
        arr += [[]]
        for j in range(0, BYTESCOUNT*8): #number of bits per word
            arr[i] += [0]

def fetch(nr):
    global cuvantControl 
    cuvantControl = 
    
def decode():

    
def execute():


def load(output):
    global seld
    global arr
    match seld:
        case [0, 0, 0]:
            arr[0] = output
        case [0, 0, 1]:
            arr[1] = output
        case [0, 1, 0]:
            arr[2] = output
        case [0, 1, 1]:
            arr[3] = output
        case [1, 0, 0]:
            arr[4] = output
        case [1, 0, 1]:
            arr[5] = output
        case [1, 1, 0]:
            arr[6] = output
        case [1, 1, 1]:
            arr[7] = output
    
    

def DATA_PATH():
    print(arr)

    # output = UAL(busA, busB, opr)
    load(output)
    

initializeRegisters()
print(arr)