inp = open("input").readlines()

milk = []
cereal = 0

for l in inp:
    _, s_bm, s_bc = l.split(",")
    bm = int(s_bm)
    bc = int(s_bc)

    cereal += bc

    if cereal >= 100 and sum(milk) >= 100:
        cereal -= 100
        for i,c in enumerate(milk):
            if c >= 100:
                milk[i] -= 100

    milk.append(bm)
    if len(milk) > 5:
        milk.pop(0)

print(sum(milk) + cereal)
