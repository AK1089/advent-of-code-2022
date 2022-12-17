# 27:27 to solve part 1, a further 9:01 to solve part 2
# some tidying (ie combining files and formatting) done after the fact

# are we doing part 2?
PART_2 = True

# reads in file input
with open("l_day12.txt") as f:
    filetext = f.read().splitlines()

# width and height of the grid, and an alphabet constant for indexing
WIDTH, HEIGHT = len(filetext[0]), len(filetext)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# the heightmap, set to all 0 for now, with a ring of "padding" too high to access on all four sides
heightmap = [[30 for x in range(WIDTH + 2)]] + [[30] + [0 for x in range(WIDTH)] + [30] for y in range(HEIGHT)] + [[30 for x in range(WIDTH + 2)]]
# the number of steps needed to access each cell on the heightmap. this is always less than the total number of cells, ie W*H.
steps_needed = [[WIDTH * HEIGHT for x in range(WIDTH + 2)] for y in range(HEIGHT + 2)]

# two blank lists for only checking the cells we've found with path length L
just_accessed = []
just_accessed_temp = []

# every (x, y) in the non-padded section of the heightmap (the actual grid)
for x in range(1, WIDTH + 1):
    for y in range(1, HEIGHT + 1):

        # match the relevant letter from the original input
        match filetext[y-1][x-1]:

            # if it's the start cell, the height can be left unchanged (set to 0 by default).
            # thus in part 2, no further action is needed. in part 1, we should flag it as needing no steps to access.
            # we should also put it in just_accessed, to kick off the algorithm.
            case "S":
                if not PART_2:
                    steps_needed[y][x] = 0
                    just_accessed.append((x, y))

            # the ending has height 25, so we can set this value directly. in part 2, we want this to be
            # the starting cell, so do what we did in the part 1 case for the start cell.
            # in part 1, we want to set this as the target.
            case "E":
                heightmap[y][x] = 25

                if PART_2:
                    steps_needed[y][x] = 0
                    just_accessed.append((x, y))
                else:
                    TARGET = (x, y)
                
            # if it's anything else, just set its height in heightmap (0 for a up to 25 for z).
            case char:
                heightmap[y][x] = ALPHABET.index(char)

# the part 1 operation: find the number of cells from S to E
if not PART_2:

    # while we haven't found a route to the target yet, look at all the cells we now know the way to
    while TARGET not in just_accessed:
        for x, y in just_accessed:

            # the path length to any neighbours is the path length to this cell, plus one more step.
            path_length = steps_needed[y][x] + 1

            # neighbours can be at most one step up
            max_height = heightmap[y][x] + 1

            # for every neighbouring cell
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):

                # if this is a more efficient route, and it's accessible
                if path_length < steps_needed[b][a] and heightmap[b][a] <= max_height:

                    # we have a new best route of length path_length to the new cell
                    steps_needed[b][a] = path_length

                    # uses a temporary list to avoid mutating just_accessed while iterating through it
                    just_accessed_temp.append((a, b))
        
        # when we're done looping, set the list to the new copy, and reset the old list 
        just_accessed = just_accessed_temp.copy()
        just_accessed_temp = []
    
    # after the loop, we have just accessed TARGET, so we can find the number of steps from our list.
    part1_answer = steps_needed[TARGET[1]][TARGET[0]]
    print(f"We required {part1_answer} steps to travel from S to E.")

# the part 2 operation: the cell of height 0 which needs the fewest steps to get to E.
else:

    # dummy target variable to indicate we haven't found a working cell yet
    TARGET = (0, 0)
    while TARGET == (0, 0):

        # same as in the part 1 case - iterate through all cells we now have a route from.
        # this time, we require a height of at least 1 less than the cell we're on, to climb up.
        for x, y in just_accessed:
            path_length = steps_needed[y][x] + 1
            req_height = heightmap[y][x] - 1

            # check all neighbouring cells
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):

                # if they're closer, and the height is enough, and we're not on a padding cell
                if path_length < steps_needed[b][a] and heightmap[b][a] >= req_height and heightmap[b][a] != 30:

                    # we can access the end in path_length steps
                    steps_needed[b][a] = path_length
                    just_accessed_temp.append((a, b))

                    # if the height is 0, we've found a working cell! set it to TARGET, and exit the loop
                    if not heightmap[b][a]:
                        TARGET = (a, b)
                        break
        
        # reset the variables as in part 1
        just_accessed = just_accessed_temp.copy()
        just_accessed_temp = []

    # outputs the answer, now that TARGET has been found.
    part2_answer = steps_needed[TARGET[1]][TARGET[0]]
    print(f"Cell {TARGET} needs only {part2_answer} steps to travel to E, and is of the lowest elevation.")
