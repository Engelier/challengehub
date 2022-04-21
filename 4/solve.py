import math

#inp = 15
inp = 987820


def get_factors(num: int) -> set:
    f = {num}
    for c in range(2, int(math.sqrt(num)) + 2):
        if num % c == 0:
            f.add(c)
            f.add(num // c)

    return f


ans = 0
inp_factors = get_factors(inp)
print(inp_factors)
for i in range(1, inp):
    shared = False
    for x in get_factors(i):
        if x in inp_factors:
            shared = True
            break

    if not shared:
        ans += i

print(ans)
