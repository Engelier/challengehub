#inp = "UDRR"
inp = "LDRDLRDRDDRLRLDLLLUULURURLDULUUDRRDDRUDDRLRRULRDUDRUDRRLRDLDRULLDUUULDRRLDDLURLURRURLRLRUULDULDLLLUDLULDUUUDLDLLUUULDDLUURDUDDRULRULRULRDULRULULRLRDRDRULLRDRRRULLRDRDDRDULDDDUUDDRDRLRRRUUDDDULULLULURURLURULRDRUDLULRULLRRLLLRRRLRRLUULDUUUULLRDRRUULULURRURDRLDLLRUDULDRULDDRURLDRDLRRULRDRRUDRURULDURRULDLDULRLLLRLUURDLUUURUDLRLUUULULULUDRRDRUDLUDLRUUUDRRDDLLUDLDURDLRRRDRDLRLRRUDLRDRUUDULLDDRRUUDDRDRDLDRLLRRRUDLRDRUDDRURLLLDDLRRDUDDUDULURDLULDDLDRRRLLLRLDUURDUDULDDRRDRDLLDRDRRLLULLLRLURLLDDLDLRDUUUDR"

room = [
    [' ', ' ', '#', '#', ' ', ' '],
    [' ', '#', '#', '#', '#', ' '],
    ['#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#'],
    [' ', '#', '#', '#', '#', ' '],
    [' ', ' ', '#', '#', ' ', ' '],
]
moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1),
}

pos = (0, 2)
sum = 0
for move in inp:
    newpos = (pos[0] + moves[move][0], pos[1] + moves[move][1])
    if 0 <= newpos[0] <= 5 and 0 <= newpos[1] <= 5 and room[newpos[0]][newpos[1]] == '#':
        pos = newpos

    sum += pos[0] + pos[1]

print(sum)
