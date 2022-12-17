# gets the file input
with open("i_day9.txt") as f:
    filetext = f.read()

# all the positions which the tail has been in
unique_tail_positions = []

# the length of the rope (2 in part 1, 10 in part 2)
ROPE_LENGTH = 10

# the position of each piece of the rope is represented by a complex number on a standard Cartesian grid.
# the start position is represented by the complex number 0 for all pieces of the rope.
positions = [0 for _ in range(ROPE_LENGTH)]

# right is one unit along the positive real axis, up is one unit along the positive imaginary axis, etc.
directions = {"R": 1,
              "L": -1,
              "U": 1j,
              "D": -1j,
}

# this dictionary determines how a piece should move according to the offset between it and the piece before it.
correction = {
              # if it's within 1 unit in each direction, don't move this piece
              0: 0,
              1: 0,
              1j: 0,
              -1: 0,
              -1j: 0,
              1+1j: 0,
              1-1j: 0,
              -1+1j: 0,
              -1-1j: 0,
              # if it's 2 units in a straight line, go one unit in that direction
              2: 1,
              2j: 1j,
              -2: -1,
              -2j: -1j,
              # if it needs to move a diagonal to catch up (if it's a knight move or 2 diagonal units away)
              2+2j: 1+1j,
              2+1j: 1+1j,
              1+2j: 1+1j,
              2-2j: 1-1j,
              2-1j: 1-1j,
              1-2j: 1-1j,
              -2+2j: -1+1j,
              -2+1j: -1+1j,
              -1+2j: -1+1j,
              -2-2j: -1-1j,
              -2-1j: -1-1j,
              -1-2j: -1-1j}


# for each instruction in the input
for line in filetext.split("\n"):

    # get the direction (R, L, U, D) of the instruction, as well as how many units
    dir, length = line.split(" ")

    # repeat the specified number of times
    for _ in range(int(length)):

        # move the head by the direction specified
        positions[0] += directions[dir]

        # for every piece which isn't the head
        for i, x in enumerate(positions):
            if i > 0:

                # move it by the correction factor listed in the dictionary
                positions[i] += correction[positions[i - 1] - x]

        # put the tail position in the list of all tail positions
        unique_tail_positions.append(positions[-1])

# len(set(iterable)) counts unique elements, ie our answer.
print(f"The tail visits {len(set(unique_tail_positions))} unique locations.")
