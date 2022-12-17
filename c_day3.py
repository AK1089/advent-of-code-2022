# reads in file input
with open("c_day3.txt") as f:
    filetext = f.read()

# the sum of the priorities of the characters found by:
# extracting the single element (using "i,") in the intersection of the sets:
# first half of the line and second half of the line
# for each line
# (we may assume, from the input, that this is unique).
p1 = (sum(
    [" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i)
    for i, in
    [set(line[:(len(line)//2)]).intersection(
        set(line[(len(line)//2):])) 
        for line in filetext.split("\n")]]))


# more readable version is shown here in triple quotes, but just for fun here's a list comprehension version too:
"""
suitcases = filetext.split("\n")
triples = [j for j in zip(*[suitcases[i::3] for i in range(3)])]
overlaps = [set(a).intersection(set(b)).intersection(set(c)) for a, b, c in triples]
print(sum([" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i) for i, in overlaps]))
"""

# print the sum of the priorities of the relevant elements, found by
# - splitting the lines into groups of (0,3,6,9...), (1,4,7,10...), (2,5,8,11...)
# - zipping these groups together to get [(0, 1, 2), (3, 4, 5), (6, 7, 8) ...]
# - iterating through these triples using a, b, c
# - finding the element in the intersection of a, b, c's sets (given uniqueness)
# - extracting this single element and calculating it's priority
p2 = (sum(
    [" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i)
    for i, in
    [set(a).intersection(set(b)).intersection(set(c))
    for a, b, c in
    [j for j in
    zip(
        *[filetext.split("\n")[k::3]
        for k in range(3)])]]]))

# prints these answers.
print(f"The answer to part 1 is {p1}.")
print(f"The answer to part 2 is {p2}.")