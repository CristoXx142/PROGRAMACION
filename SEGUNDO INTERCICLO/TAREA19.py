zork = 0
print('antes', zork)
for objeto in [9, 41, 12, 3, 74, 15]:
    if objeto > zork:
        zork = zork + 1
    print(zork, objeto)
print('después', zork)
