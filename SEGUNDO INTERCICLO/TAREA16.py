while True:
    line= input('>')
    if line[0] == '#':
        continue
    if line == '0':
        break
    print(line)
print('fin del programa')

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')