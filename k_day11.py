# reads in file input, separated into monkey descriptions
with open("k_day11.txt") as f:
    filetext = f.read().split("\n\n")

# monkey class!
class Monkey:
    def __init__(self, description) -> None:
        
        # for each line, get information about the monkey
        lines = description.split("\n")
        for line in lines:
            match line.strip().split(" "):

                # eg. "Monkey 2:" -> number = 2
                case ["Monkey", num]:
                    self.number = int(num[0])
                
                # eg. "Starting items: 34, 87, 2, 14" -> items = [34, 87, 2, 14]
                case ["Starting", "items:", *values]:
                    self.items = [int(v.replace(",", "")) for v in values]

                # eg. "Operation: new = old + 4" -> operation = "new = old + 4"
                case ["Operation:", *args]:
                    self.operation = " ".join(args)

                # eg: "Test: divisible by 7" -> test = 7
                case ["Test:", "divisible", "by", num]:
                    self.test = int(num)

                # eg. "If true: throw to monkey 4" -> true_throw = 4
                case ["If", "true:", "throw", "to", "monkey", num]:
                    true_throw = int(num)
                
                # eg. "If false: throw to monkey 6" -> false_throw = 6
                case ["If", "false:", "throw", "to", "monkey", num]:
                    false_throw = int(num)

        # stores the monkey's throw directions, and how many inspections it has so far
        self.throw = (true_throw, false_throw)
        self.inspections = 0

    # all details about the monkey, formatted nicely
    def __repr__(self) -> str:
        return f"Monkey #{self.number}: has items {self.items}, operation '{self.operation}', test number {self.test}, and throw targets {self.throw}"


# creates Monkey objects according to the file
monkeys = []
for monkey in filetext:
    monkeys.append(Monkey(monkey))

# are we doing part 2?
PART_2 = True
rounds = 10000 if PART_2 else 20

# for each round, do the process for each monkey in turn
for round in range(rounds):
    for monkey in monkeys:

        # it inspects one time for each item!
        monkey.inspections += len(monkey.items)

        # inspect all the items, calling their value "old"
        for old in monkey.items:

            # eg. if operation = "new = old + 5", this runs that code, setting new to the value of old + 5
            exec(monkey.operation)

            # worry level divided by 3
            if not PART_2:
                new = new // 3

            # keeps values manageable (for part 2): this number is 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
            new = new % 9_699_690
            
            # if test passes, throw to True monkey, otherwise throw to False monkey
            if new % monkey.test == 0:
                monkeys[monkey.throw[0]].items.append(new)
            else:
                monkeys[monkey.throw[1]].items.append(new)

        # now the monkey has thrown all its items, so clear its items
        monkey.items = []

    # progress tracker!
    if (round + 1) % 1000 == 0:
        print(f"Completed {round + 1} rounds!")

# print the number of inspections for the two most active monkeys
most_active_a, most_active_b = (sorted([monkey.inspections for monkey in monkeys], reverse=True)[:2])
print(f"\nThe two most active monkeys have scores of {most_active_a} and {most_active_b}.")
print(f"This gives a monkey business score of {most_active_a * most_active_b}.")