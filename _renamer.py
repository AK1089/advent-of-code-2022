# gets all my files in a nice order!
from os import rename, getcwd
from os.path import join

# all letters (a in position 1, b in position 2 etc.)
alphabet = " abcdefghijklmnopqrstuvwxyz"
extensions = (".txt", "n.txt", ".py")

# working directory
cwd = getcwd()

# for every possible filename, eg. day4.py or day17.txt
for date in range(1, 26):
    for ext in extensions:

        # old and new filenames
        src = join(cwd, f"day{date}{ext}")
        dst = join(cwd, f"{alphabet[date]}_day{date}{ext}")

        # runs the rename command
        try:
            rename(src, dst)
            print(f"Renamed {src.split('/')[-1]} to {dst.split('/')[-1]}!")
        except FileNotFoundError:
            print(f"Couldn't find file {src} - skipped!")
