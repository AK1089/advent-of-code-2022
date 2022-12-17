# reads in file input
with open("d_day4.txt") as f:
    filetext = f.read()

# counts of overlapping / fully overlapping pairs as specified in both parts (part 1: acount and part 2: bcount)
acount = 0
bcount = 0

# for each line in the input
for line in filetext.split("\n"):

    # separate into the first two and last two, and separate these numbers into a, b, c, d
    # such that the first elf goes a-b and the second goes c-d
    (a, b), (c, d) = [x.split("-") for x in line.split(",")]

    # if a-b is entirely within c-d, or vice versa, add one to part 1's count
    if (int(a) >= int(c) and int(b) <= int(d)) or (int(a) <= int(c) and int(b) >= int(d)):
        acount += 1

    # unless the first elf stops before the second elf starts, or vice versa, there has to be an overlap
    # so we can add one to part 2's count
    if not ((int(b) < int(c)) or (int(d) < int(a))):
        bcount += 1

# prints these answers.
print(f"The answer to part 1 is {acount}.")
print(f"The answer to part 2 is {bcount}.")