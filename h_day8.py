# gets the file input
with open("h_day8.txt") as f:
    filetext = f.read()

# gets a 2D array view from both perspectives
rows = [[c for c in line] for line in filetext.split("\n")]
w, h = len(rows[0]), len(rows)
cols = [[r[i] for r in rows] for i in range(w)]

# all cells are visible by default, we'll find invisible ones later
visible_count = w * h
max_scenic_score = 0

# for each cell in the grid that's not on the edge
for x in range(1, w-1):
    for y in range(1, h-1):
        tree_height = rows[y][x]

        # note that rows[y][x] == cols[x][y]] for all x, y
        # invisible if not the maximum of its sublists so far and beyond

        # visible from right/left?
        if max(rows[y][:x]) >= tree_height <= max(rows[y][x+1:]):
            if max(cols[x][:y]) >= tree_height <= max(cols[x][y+1:]):
                visible_count -= 1

        # the scenic distances in each direction, and the actual sequence of trees in each direction
        distances = [0, 0, 0, 0]
        directions = [rows[y][:x][::-1], rows[y][x+1:], cols[x][:y][::-1], cols[x][y+1:]]

        # for each direction 0-3 (listed in directions)
        for i, path in enumerate(directions):

            # for each numbered tree in that direction
            for j, t in enumerate(path):

                # if it's tall enough to block the view, you can see that number of trees before it,
                # plus the tree itself, ie j+1 trees are visible in that direction
                if t >= tree_height:

                    # set the number of trees visible in that direction, and break out of the loop
                    distances[i] = j + 1
                    break

            # if we haven't broken out of the loop, all the trees are visible!
            else:
                distances[i] = len(path)
        
        # scenic score based on visible trees in each direction
        scenic_score = distances[0] * distances[1] * distances[2] * distances[3]

        # if we have a new record
        if scenic_score > max_scenic_score:
            max_scenic_score_data = (x, y, tree_height, distances)
            max_scenic_score = scenic_score


# outputs the answers
print(f"there are {visible_count} trees visible from the edges.")
print(f"the best tree is the tree of height {max_scenic_score_data[2]} at position ({max_scenic_score_data[0]},{max_scenic_score_data[1]}).")
print(f"this has a score of {max_scenic_score} (directional counts: {max_scenic_score_data[3]}).")