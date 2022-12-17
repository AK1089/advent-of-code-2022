# how many points each setup gives you, according to part 1's scoring system
points1 = {
    "A X":4,
    "A Y":8,
    "A Z":3,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":7,
    "C Y":2,
    "C Z":6,
    }

# how many points each setup gives you, according to part 2's scoring system
points2 = {
    "A X":3,
    "A Y":4,
    "A Z":8,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":2,
    "C Y":6,
    "C Z":7,
    }

# gets input file and reads it line by line
with open("b_day2.txt") as f:
    filetext = f.read().split("\n")

# scores for each line for parts 1 and 2
scores1 = [points1[line] for line in filetext]
scores2 = [points2[line] for line in filetext]

# outputs answer
print(f"In part 1, you get {sum(scores1)} points.")
print(f"In part 2, you get {sum(scores2)} points.")
