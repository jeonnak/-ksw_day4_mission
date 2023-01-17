# 7.11

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"

# 첫 번째

# start1[0] = start1[0] + '!'
# start1[1] = start1[1] + '!'
# start1[2] = start1[2] + '!'
# rhymes[0][0] = rhymes[0][0] + ' !'
# rhymes[1][0] = rhymes[1][0] + ' !'
# rhymes[2][0] = rhymes[2][0] + ' !'
# rhymes[3][0] = rhymes[3][0] + ' !'
# rhymes[4][0] = rhymes[4][0] + ' !'
# rhymes[5][0] = rhymes[5][0] + ' !'
# rhymes[6][0] = rhymes[6][0] + ' !'

start1[0] = start1[0].title()
start1[1] = start1[1].title()
start1[2] = start1[2].title()

print(rhymes[0]+rhymes[1]+rhymes[2]+rhymes[3]+rhymes[4]+rhymes[5]+rhymes[6])

# rhymes[0][0] = rhymes[0][0].title()
# rhymes[1][0] = rhymes[1][0].title()
# rhymes[2][0] = rhymes[2][0].title()
# rhymes[3][0] = rhymes[3][0].title()
# rhymes[4][0] = rhymes[4][0].title()
# rhymes[5][0] = rhymes[5][0].title()
# rhymes[6][0] = rhymes[6][0].title()


print(start1)
print('! '.join(start1) + '! ' + rhymes[0][0] + '!')
print()
print('! '.join(start1) + '! ' + rhymes[1][0] + '!')

print('! '.join(start1) + '! ' + rhymes[2][0] + '!')

print('! '.join(start1) + '! ' + rhymes[3][0] + '!')

print('! '.join(start1) + '! ' + rhymes[4][0] + '!')

print('! '.join(start1) + '! ' + rhymes[5][0] + '!')

print('! '.join(start1) + '! ' + rhymes[6][0] + '!')
print(rhymes)

print(rhymes[0][0])