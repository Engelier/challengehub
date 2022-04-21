#inp = open("test_input").readlines()
#source = "A"
#target = "C"
inp = open("input").readlines()
source = "DIDDY"
target = "TUPAC"

network = {}
for l in inp:
    a, b, cost = l.split(",")
    if a in network:
        network[a].append((b, int(cost)))
    else:
        network[a] = [(b, int(cost))]


def get_min_cost(s, t, c, v):
    v.add(s)
    if s == t:
        return c

    min_cost = 1e9
    for n in network[s]:
        if n[0] in v:
            continue
        this_min_cost = get_min_cost(n[0], t, c + n[1], v.copy())
        if this_min_cost < min_cost:
            min_cost = this_min_cost

    return min_cost


print(get_min_cost(source, target, 0, set()))
