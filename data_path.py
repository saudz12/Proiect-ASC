import numpy as np
from variables import *

#print(registers) #cehck if variables works right

#dont have UCC and RAM so we made something up
#for tests the user imputs something like
#XOR 1 2 ADD 1 2
#and we get
#01011001010001

def interpret(command : str):
    global regInstruc
    global MUXSIZE
    
    arr = []
    arr = command.split()
    match len(arr):
        case 1:
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
                destination += [aux[i]]
                
            aux = []
            val = int(arr[2])
            
            for bit in bin(val): 
                aux += [bit]
            aux = aux[2:]
            start = len(aux) - MUXSIZE
            if start < 0:
                start = 0
            for i in range(len(aux) - MUXSIZE, len(aux)):
                source += [aux[i]]
            
            regInstruc += destination + source + destination
            
    #regInstruc = [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0] #mock    

def fetch(nr):
    global regInstruc
    global curInstruc
    curInstruc = regInstruc[nr:(nr+3*MUXSIZE+OPRSIZE)]
    return
    
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
    opr = curInstruc[0:OPRSIZE]
    selA = curInstruc[OPRSIZE:(OPRSIZE+MUXSIZE)]
    selB = curInstruc[(OPRSIZE+MUXSIZE):(OPRSIZE+2*MUXSIZE)]
    selD = curInstruc[(OPRSIZE+2*MUXSIZE):(OPRSIZE+3*MUXSIZE)]
    return
    
def execute():
    busA = registers[int(''.join(str(i) for i in selA), 2)]
    busB = registers[int(''.join(str(i) for i in selB), 2)]
    # output = UAL(busA, busB, opr)
    return 

def load(output):
    global selD
    global registers
    poz = int(''.join(str(i) for i in selD), 2)
    if poz == 0:
        info = int(''.join(str(i) for i in output), 2)
        print(info)
    else:
        registers[poz] = output
    return
    
'''
initializeRegisters()
print(arr)
'''