# gets file input text, split by double line breaks to separate into different elves
with open("a_day1.txt") as f:
    elves = f.read().split("\n\n")

    # for each elf, get the sum of the numbers on each line
    calories = [sum([int(i) for i in elf.split("\n")]) for elf in elves]

    # output answers to parts 1 and 2
    print(f"The elf with the largest total has {max(calories)} calories.")
    print(f"The three elves with the largest totals have {sum(sorted(calories, reverse=True)[:3])} calories together.")
