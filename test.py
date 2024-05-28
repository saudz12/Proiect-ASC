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
print(dp.selD)
'''

commands = "ADD 5 6"

dp.interpret("IN 5 11")
dp.fetch(0)
dp.decode()
dp.execute()
dp.load()

dp.interpret("IN 6 12")
dp.fetch(1)
dp.decode()
dp.execute()
dp.load()

dp.interpret(str(commands))
dp.fetch(2)
dp.decode()
dp.execute()
dp.load()

dp.interpret("OUT 5 0")
dp.fetch(3)
dp.decode()
dp.execute()
dp.load()

cnt = 4

while(True):
    commands = input()
    #print(commands)
    if commands.split(' ')[0] == "STOP":
        break
    dp.interpret(str(commands))
    dp.fetch(cnt)
    dp.decode()
    dp.execute()
    dp.load()
    cnt += 1

#print(dp.registers[5], dp.registers[6])

print(int(''.join(str(i) for i in [0, 0, 1, 0, 1, 0]), 2))

'''while(commands.split(" ")[0] != "STOP"):
    commands = input()
    print(commands)'''



