# useful objects to get items from a nested dictionary
from functools import reduce
from operator import getitem

# reads the file input
with open("g_day7.txt") as f:
    filetext = f.read()

# the directory and current path
base = {"/":{}}
path = ["/"]

# tracking variables for puzzle answers
small_directories_total_size = 0
smallest_deletable_directory_size = 70000000

# match each instruction to a type of line
for instruction in filetext.split("\n"):
    match instruction.split(" "):

        # cd /, cd .., cd dir
        case ["$", "cd", cmd]:

            # return to base path directory
            if cmd == "/":
                path = ["/"]
            # go back one step
            elif cmd == "..":
                path = path[:-1]
            # enter the specified directory
            else:
                path.append(cmd)

        # $ ls - do nothing
        case ["$", "ls"]:
            pass
        
        # some listed directory: add an empty dictionary at that path
        case ["dir", dirname]:
            reduce(getitem, path, base)[dirname] = {}

        # some listed file: list it in the dictionary path with its size
        case [size, filename]:
            reduce(getitem, path, base)[filename] = int(size)

# gets the size of the directory specified by dirpath
def getsizeof(dirpath):

    # our puzzle answer tracking variables
    global small_directories_total_size, smallest_deletable_directory_size
    
    # gets our dictionary and sets its size to zero
    dir = reduce(getitem, dirpath, base)
    size = 0

    # for each item in our directory, add its size directly if a file or
    # its size calculated the same way if a directory.
    for key, value in dir.items():
        if isinstance(value, int):
            size += value
        else:
            size += getsizeof(dirpath + [key])

    # if it's a small directory, add its size to the total we're tracking
    if size <= 100000:
        small_directories_total_size += size

    # if deleting it would free up enough space, and it's smaller, record it
    if size >= 30000000 + 41735494 - 70000000:
        smallest_deletable_directory_size = min(smallest_deletable_directory_size, size)

    # size of the specified directory
    return size

# outputs the answers
print("The total size of the filesystem is", getsizeof(["/"]), end=".\n")
print("The total size of all small directories is", small_directories_total_size, end=".\n")
print("The smallest directory that would free up enough space has size", smallest_deletable_directory_size, end=".\n")

# a fun bonus to view the filesystem in the same way as the example shows
def display_filesystem(dirpath):

    # does the indentation based on nesting level, then the name and the directory
    print(f"{' ' * (len(dirpath) * 2 - 2)}- {dirpath[-1]} (dir)")

    # for each file or directory in our file system
    for k, v in reduce(getitem, dirpath, base).items():

        # if it's a file (its value is an int and not a dict), just print it out as specified
        if isinstance(v, int):
            print(f"{' ' * (len(dirpath) * 2)}- {k} (file, size={v})")

        # otherwise, just display it! everything works as normal
        else:
            display_filesystem(dirpath + [k])

# the output of this is in day7n.txt - it's quite long so I've commented the line out for now.
# display_filesystem(["/"])