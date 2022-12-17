# gets the file input
with open("j_day10.txt") as f:
    filetext = f.read()

# a generator object: next(instrs) returns the next instruction
instrs = (i for i in filetext.split("\n"))

# X is the current value of the register, toadd is the value that is going to be added next
X, toadd = 1, 0

# cycle is the current cycle count, delay is how long until the next instruction
cycle, delay = 0, 0

# sdss counts the total value asked for in part 1. CRT stores whether the sprite should be drawn at each cycle
six_defined_signal_strengths = 0
CRT = []

# prints out our answers
def output():

    # part 1 answer is output directly
    print(f"\n\nThe total signal strength at the six defined positions is {six_defined_signal_strengths}.")

    # part 2 answer needs to be extracted from the CRT boolean list
    print("\nThe CRT monitor displays the following picture:\n")

    # for each value in the CRT list, if it's True print out a symbol, otherwise print out a space (without a newline)
    for i, x in enumerate(CRT):
        print("█" if x else " ", end="")

        # switch to the next line every 40 symbols
        if i % 40 == 39:
            print()
    
    # formatting to make it look nicer
    print("\n")


# keep running cycles until you exhaust the instructions!
while True:
    cycle += 1

    # if we're in the "delay" phase (ie the first cycle of an addx instruction), just reduce the remaining delay by 1
    if delay:
        delay -= 1

    # if there's no delay to wait out, add the value in toadd
    # (this will be 0 if we are running noop)
    else:
        X += toadd

        # try to get the next instruction 
        try:
            curr = next(instrs)

        # if we've run out, print out our answers and end the program
        except StopIteration:
            output()
            break

        # resets the delay and toadd so we can calculate these
        delay = toadd = 0

        # if noop, then delay and toadd stay 0, so only change these if running addx
        if curr.startswith("addx"):

            # we have to wait a phase before adding toadd (which is the second argument given after addx)
            delay = 1
            toadd = int(curr.split(" ")[1])
    
    # if this is a special cycle we're looking out for, record its value as desired
    if (cycle + 20) % 40 == 0:
        six_defined_signal_strengths += X * cycle

    # originally for debugging purposes - prints out what's going on (spammy, so commented out)
    # print(f"cycle number {cycle}: delay {delay} until {toadd}, X={X}, running {curr}")

    # adds True to CRT only if the horizontal position of the cycle is within 1 of X (otherwise False)
    CRT.append((((cycle - 1) % 40) - X) in (-1, 0, 1))
