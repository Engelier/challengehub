#bgcolor = 'kdb4life'
bgcolor = 'do you think that maybe like, 1 in 10 people could be actually robots?'

zeroed = ''
for s in bgcolor:
    if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']:
        zeroed += s
    else:
        zeroed += '0'

zeroed += "0" * (3 - (len(zeroed) % 3))

answer = zeroed[0:len(zeroed) // 3][:2] + zeroed[len(zeroed) // 3:len(zeroed) // 3 * 2][:2] + zeroed[len(zeroed) // 3 * 2:][:2]

print(answer)
