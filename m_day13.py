# 46:52 for part 1, a further 9:46 for part 2

# reads in file input
with open("m_day13.txt") as f:
    filetext = f.read().splitlines()

# the nonblank lines of the puzzle, each as lists added to the variable lines
lines = []
for line in filetext:

    # removes nonblank lines and adds them as lists using exec
    if line: exec(f"lines.append({line})") 

# a recursive compare function which takes in two items to compare (lists, integers, or one of each)
def compare(left, right):

    # 2 means both are numbers, so compare directly.
    # 0 means both are lists, so compare item-wise.
    # 1 means one of each, so convert the integer to a single-item list and compare item-wise.
    option = isinstance(left, int) + isinstance(right, int)

    # both are numbers: return True/False if the test is conclusive, otherwise None
    if option == 2:
        if left < right: return True
        elif left > right: return False
        else: return None

    # now we know at least one is a list, so if we have an integer and a list, convert them to single-item lists.
    # for example, if left is an integer, we make a list called left with value [left].
    if isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]
    
    # make each of these into generators instead of lists, to call on next
    left_gen = (i for i in left)
    right_gen = (i for i in right)

    # keep running the test until you get some sort of result - we always return eventually, because at some point
    # left or right run out of items (being finite), leading to a StopIteration (and hence a return).
    while True:

        # try getting the next item from the left list
        try: l = next(left_gen)

        # if we've run out of items, we need to do an extra check:
        except StopIteration:

            # does the right list also run out of items at the same step? if so, the test is inconclusive, so None.
            try: r = next(right_gen)
            except StopIteration: return None

            # if it doesn't, then the right list is longer, so return True (correct order)
            return True

        # now the left list hasn't run out of items, so if the right list does then it must be shorter.
        # this means the left list is longer, so return False.
        try: r = next(right_gen)
        except StopIteration: return False

        # the length test wasn't conclusive here, so compare elements. take l and r (our next elements from each)
        # and run the compare function on them. if the test is conclusive, we have our answer, otherwise keep going.
        if (test := compare(l, r)) is not None:
            return test


# a list storing which pairs are in order, with an extra item to enable 1-indexing (which is False, and so not counted later).
# for each pair of lines, compare them to get a result (True being in order, False being not).
pairs_in_order = [False] + [compare(x, y) for x, y in zip(*[lines[k::2] for k in range(2)])]

# outputs the answer: the sum of the indices of the pairs which are True, ie. in order.
print(f"The sum of the indices of correctly ordered pairs is {sum([i for i, test in enumerate(pairs_in_order) if test])}.")

# for part 2, we need the two extra divider packets, as specified, and a blank list to sort compared lines
lines.append([[2]])
lines.append([[6]])
sorted_lines = []

# for each packet (including our two new divider packets)
for line in lines:

    # for each comparison line that has already been sorted into an order
    for i, comparison in enumerate(sorted_lines):

        # if the line does not go before the comparison line which has already been sorted,
        if compare(line, comparison):

            # place it immediately after and end the loop
            sorted_lines = sorted_lines[:i] + [line] + sorted_lines[i:]
            break

    # if we get to the end and it hasn't been placed, place it at the end
    else: sorted_lines.append(line)

# find where our dividers have gone (add one for 1-indexing)
first_divider, second_divider = sorted_lines.index([[2]]) + 1, sorted_lines.index([[6]]) + 1
print(f"Of the {len(sorted_lines)} packets, the divider packets are in position {first_divider} and {second_divider}.")
print(f"This makes the decoder key {first_divider * second_divider}.")
