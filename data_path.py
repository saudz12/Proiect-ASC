import numpy as np
from variables import *
import ALU

#print(registers) #cehck if variables works right

#dont have UCC and RAM so we made something up
#some type of interpreter
#for tests the user imputs something like
#XOR 1 2 ADD 1 2
#and we get
#0101100101000100111001010001 as operation code - check NOTITE SEMINAR 10

#int(''.join(str(i) for i in selD), 2) from bit array to number!!!

usrInput : int
callInput : bool

def interpret(command : str):
    global regInstruc
    global MUXSIZE
    
    arr = []
    arr = command.split()
    match len(arr):
        case 1:
            exit(0)
        case 2:
            if arr[0] != "OUT":
                exit(0)
        case 3:
            regInstruc += codes[arr[0]]
            
            source = []
            destination = []
            
            aux = []
            val = int(arr[1])
            
            for bit in bin(val): 
                aux += [bit]
            aux = aux[2:]
            start = len(aux) - MUXSIZE
            if start < 0:
                start = 0
            for i in range(start, len(aux)):
                destination += [int(aux[i])]
                
            regInstruc += destination    
            
            aux = []
            val = int(arr[2])
            
            for bit in bin(val): 
                aux += [bit]
            aux = aux[2:]
            start = len(aux) - MUXSIZE
            if start < 0:
                start = 0
            for i in range(len(aux) - MUXSIZE, len(aux)):
                source += [int(aux[i])]
                
            regInstruc += source
            
            if arr[0] == "OUT":
                destination = []
                for i in range(0, 8*BYTESCOUNT):
                    destination += [0]
            
            regInstruc += destination 
            
    #regInstruc = [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0] #mock    

#FETCH stage - gets the next sleection of OPRSIZE+3*MUXSIZE bits from instruction register
def fetch(nr):
    global regInstruc
    global curInstruc
    curInstruc = list(regInstruc[nr:(nr+3*MUXSIZE+OPRSIZE)])
    return
    
#DECODE stage - 
def decode():
    #primii OPRSIZE biti: operation code 
    #urm MUXSIZE biti: SELA
    #urm MUXSIZE biti: SELB
    #urm MUXSIZE biti: SELD
    
    global curInstruc
    global opr
    global selA
    global selB
    global selD
    
    opr = list(curInstruc[0:OPRSIZE])
    selA = list(curInstruc[OPRSIZE:(OPRSIZE+MUXSIZE)])
    selB = list(curInstruc[(OPRSIZE+MUXSIZE):(OPRSIZE+2*MUXSIZE)])
    selD = list(curInstruc[(OPRSIZE+2*MUXSIZE):(OPRSIZE+3*MUXSIZE)])
    
    return
    
def execute():
    global opr
    
    busA = list(registers[int(''.join(str(i) for i in selA), 2)])
    
    busB = list(registers[int(''.join(str(i) for i in selB), 2)])
    
    output = ALU.ALU(list(busA), list(busB), list(opr))
    
    return 

def load(output):
    global selD
    global registers
    
    poz = int(''.join(str(i) for i in selD), 2)
    if poz == 0:
        info = int(''.join(str(i) for i in output), 2)
        print(info)
    else:
        registers[poz] = list(output)
    
    return
    
'''
initializeRegisters()
print(arr)
'''

'''c = [0,1,0,0,1]
a = list(c)
b = [1,0,0,1,0]
print(ALU.ALU(a, b, [0,0,1,0,0]))
print(a, b, c)'''