# 26:01 for part 1, a further 30:12 for part 2 (!)
# opens the file
with open("n_day14.txt") as f:
    filetext = f.read().splitlines()

# the rock formation: 50 units on either side L/R, and 300 units down
rock = [[False for x in range(401)] for y in range(300)]

# falling sand, represented as a complex number (two lists to avoid mutability issues)
falling = [200 + 0j]
newfalling = []

# are we doing part 2? if so, here's the floor height
PART_2 = False
floorheight = 0


# for each input line
lines = []
for line in filetext:

    # to unpack: take all but the last pair, as well as the next pair, and assign (eg. "a,b -> c,d")
    pairs = [x.split(",") for x in line.split(" -> ")]
    for i, (a, b) in enumerate(pairs[:-1]):
        c, d = pairs[i+1]

        # takes integer values, and makes the 500s into 200s (it's not that wide!)
        a, b, c, d = int(a), int(b), int(c), int(d)
        a, c = a - 300, c - 300

        # new floorheight!
        floorheight = max(floorheight, b + 2, d + 2)

        # if the x-coordinate is fixed, add rock along the y-axis
        if a == c:
            for k in range(min(b, d), max(b, d) + 1):
                rock[k][a] = True

        # and vice-versa
        if b == d:
            for k in range(min(a, c), max(a, c) + 1):
                rock[b][k] = True

# adds a floor for part 2
for x in range(401):
    rock[floorheight][x] = True

# settled bits of sand in part 1, and the original rock formation
originalrock = [l.copy() for l in rock]
settled = [0, 0]
settledmode = 0

# keep going until we break when sand starts falling forever
while True:

    # for each bit of falling sand
    for f in falling:

        # try going down
        if not rock[int(f.imag) + 1][int(f.real)]:
            newfalling.append(f + (0 + 1j))
        
        # try going down-left
        elif not rock[int(f.imag) + 1][int(f.real) - 1]:
            newfalling.append(f + (-1 + 1j)) 

        # try going down-right
        elif not rock[int(f.imag) + 1][int(f.real) + 1]:
            newfalling.append(f + (1 + 1j)) 

        # can't go anywhere, so settle, essentially turning into rock
        else:
            rock[int(f.imag)][int(f.real)] = True
            settled[settledmode] += 1

        # hit the floor (would cascade if no floor)
        if f.imag == floorheight - 1:
            settledmode = 1

    # add a new piece of falling sand, and transfer the lists
    newfalling.append(200 + 0j)
    falling = newfalling.copy()
    newfalling = []

    # sand is blocked off! part 2 is done
    if len(falling) == 1:
        break

    

# trims our data to just the floor height
rock = rock[:floorheight+1]
originalrock = originalrock[:floorheight+1]

    
# for each indexed line in the final formation, and for each indexed cell
for i, (line, orig) in enumerate(zip(rock, originalrock)):
    for j, (x, y) in enumerate(zip(line, orig)):

        # print █ if it's original rock, * if it's settled sand, ~ if it's falling sand, and a space otherwise - see n_day14n.txt
        # print("█" if y else ("*" if x else ("~" if (j + (i * 1j)) in falling else " ")), end="")
        pass
        
    # newline for formatting
    print()

# outputs answer
print(f"\nThere are {settled[0] - 1} pieces of settled sand when the cascade begins.")
print(f"There are {settled[0] + settled[1]} pieces of settled sand when the cave is blocked off.")