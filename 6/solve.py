#inp = 3
inp = 123

sum = 0
for x in range(0, inp + 1):
    for y in range(0, inp + 1 - x):
        for z in range(0, inp + 1 - x - y):
            if x + y + z == inp:
                sum += ("%d%d%d" % (x, y, z)).count("1")

print(sum)
