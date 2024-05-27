import data_path as dp

''''''

dp.initializeRegisters()
'''
dp.interpret([0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])
print(dp.regInstruc)
dp.fetch(0)
print(dp.curInstruc)
dp.decode()
print(dp.selA)
print(dp.selB)
print(dp.selD)'''

commands = "ADD 5 6"

dp.interpret("IN 5 12")
dp.interpret("IN 6 11")
dp.interpret(commands)
dp.fetch(0)
dp.decode()
dp.execute()
dp.load()
print(dp.registers[5], dp.registers[6])
print()

'''while(commands.split(" ")[0] != "STOP"):
    commands = input()
    print(commands)'''



