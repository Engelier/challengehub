#inp = "LRDLU"
inp = "LRUDDLRDLLDRUUUURLUDLLDLUDRURRDLUDRDURUURDLRULDULLRDRLLLDRDRRRLLDLRUUUDRLRDRLDRRUURDRLUDUUDUDLLDRULRLDRRLUUURRDDUDRDRURRLRRLLDRUUURLLRLRURRRUDUDURUDRURDRDDDURDLUDDLDUDRULDRULURLUULLLURDRLDUDRDUDRLDDRUULLLULRLDUURUUDRDLLDRRDRLLRUUURLDRULUDDRDDLDRURURR"

dice = [
    # F    B    L    R    U    D
    ['1', '6', '2', '5', '3', '4'],
    ['1', '6', '3', '4', '2', '5']
]

sum = 0
for i, d in enumerate(inp):
    for x in dice:
        front = x[0]
        if d == 'U':
            x[0] = x[5]
            x[5] = x[1]
            x[1] = x[4]
            x[4] = front
        elif d == 'D':
            x[0] = x[4]
            x[4] = x[1]
            x[1] = x[5]
            x[5] = front
        elif d == 'L':
            x[0] = x[3]
            x[3] = x[1]
            x[1] = x[2]
            x[2] = front
        elif d == 'R':
            x[0] = x[2]
            x[2] = x[1]
            x[1] = x[3]
            x[3] = front

    if dice[0][0] == dice[1][0]:
        sum += i

print(sum)
