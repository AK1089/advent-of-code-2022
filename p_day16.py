# reads input by line
with open("p_day16.txt") as f:
    filetext = f.read().splitlines()

from collections import defaultdict

class Valve:
    def __init__(self, name: str, rate: int, connections: tuple[str]) -> None:
        self.name = name
        self.rate = rate
        self.direct = connections
        self.connections = defaultdict(int)

valves = []

for line in filetext:
    # Valve AW has flow rate=0; tunnels lead to valves DS, AA
    _, name, _, _, rate, _, _, _, _, *conn = line.replace(",", "").split(" ")
    rate = int(rate[5:-1])
    valves.append(Valve(name, rate, conn))

print(valves)