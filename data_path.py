import numpy as np

x = 4

BYTESCOUNT = 1
REGISCOUNT = 15
MUXSIZE = 3
OPRSIZE = 5

regInstruc = []
curInstruc = []

selA = []
selB = []
selD = []

opr = []

registers = []
busA = []
busB = []

output = []
#print(registers)

def initializeRegisters():
    global registers
    for i in range(0, REGISCOUNT+1): #number of registers - depends on number of bits in SELD
        registers += [[]]
        for j in range(0, BYTESCOUNT*8): #number of bits per word
            registers[i] += [0]

def interpret(commands):
    global regInstruc
    
    regInstruc = [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0]
 
 #1 XOR 2 > 1, 1 ADD 2 > 0
 #1011000101000100100000010001      

def fetch(nr):
    global regInstruc
    global curInstruc
    curInstruc = regInstruc[nr:(nr+3*MUXSIZE+OPRSIZE)]
    
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