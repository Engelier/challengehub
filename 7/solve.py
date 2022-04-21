inp = open("input").readlines()

elo = {}
for s in inp:
    a, b, score = s.split(",")
    sa, sb = map(int, score.split("-"))
    ea = elo.get(a, 1200)
    eb = elo.get(b, 1200)

    Ea = 1 / (1 + 10 ** ((eb - ea) / 400))
    Eb = 1 / (1 + 10 ** ((ea - eb) / 400))

    if sa > sb:
        elo[a] = ea + 20 * (1 - Ea)
        elo[b] = eb - 20 * (1 - Ea)
    else:
        elo[a] = ea - 20 * (1 - Eb)
        elo[b] = eb + 20 * (1 - Eb)

print(int(max(elo.values())) - int(min(elo.values())))
