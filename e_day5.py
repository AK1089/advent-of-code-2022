# the stacks, in order (with a bonus formatting hack at the start to maintain 1-indexing)
stacks = [["Final arrangement: "], ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'], ['D', 'Q', 'L'], ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'], ['V', 'G', 'L', 'F', 'Z', 'S', 'L', 'C', 'D', 'H', 'B', 'Q', 'G'], ['V', 'G', 'L', 'F', 'Z', 'S'], ['D', 'G', 'N', 'P'], ['D', 'Z', 'P', 'V', 'F', 'C', 'W'], ['C', 'P', 'D', 'M', 'S'], ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']]

# reads the file input
with open("e_day5.txt") as f:
    filetext = f.read()

# are we doing part 2 with the updated crane?
updated = True

# for each line in the input instructions, trimmed of the crane starting data
for line in filetext.split("\n"):

    # we need only arguments 2, 4, 6 (ie move *i* from *a* to *b*)
    _, i, _, a, _, b = line.split(" ")

    # what's on the crane arm, if there are multiple things?
    oncrane = []

    # move i times as specified
    for j in range(int(i)):

        # in part 1, we just get rid of the top item from stack a and stick it on the top of stack b
        if not updated:
            stacks[int(b)].append(stacks[int(a)].pop())

        # in part b, we just put it on the crane arm for now (and take it off stack a)
        else:
            oncrane.append(stacks[int(a)].pop())

    # if we're using the crane arm, put the entire crane arm (in reverse order) on stack b
    if updated:
        stacks[int(b)] = stacks[int(b)] + oncrane[::-1]

# for each stack, output the top item (here's where our formatting hack works!)
for stack in stacks:
    print(stack[-1],end="")
print()