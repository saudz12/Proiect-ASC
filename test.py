import data_path as dp

'''dp.initializeRegisters()
dp.interpret([0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
print(dp.regInstruc)
dp.fetch(0)
print(dp.curInstruc)
dp.decode()
print(dp.selA)
print(dp.selB)
print(dp.selD)'''

commands = ""

while(commands.split(" ")[0] != "STOP"):
    commands = input()
    print(commands)



