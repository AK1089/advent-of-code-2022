# reads the file input
with open("f_day6.txt") as f:
    filetext = f.read()

# set this to the length of thing you want to check (4 for part 1, 14 for part 2)
bufferlength = 14

# for every index which specifies the start of a block of length bufferlength in the text
for i in range(len(filetext) - bufferlength + 1):

    # if the number of unique characters on that block is the length of the block
    # (ie. if all the characters are different)
    if len(set(filetext[i:i+bufferlength])) == bufferlength:

        # outputs the answer and exits the loop
        print(f"The marker ends at position {i+bufferlength}.")
        break