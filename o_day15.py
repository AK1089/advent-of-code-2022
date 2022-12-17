# reads input by line
with open("o_day15.txt") as f:
    filetext = f.read().splitlines()

# which row is it checking, and what ranges are included?
ROW_TO_CHECK = 2000000
excluded = []

# for each sensor
for line in filetext:

    # gets the sensor and closest beacon as a complex number
    _, _, sx, sy, _, _, _, _, bx, by = line.split(" ")
    sensor = int(sx[2:-1]) + int(sy[2:-1]) * 1j
    beacon = int(bx[2:-1]) + int(by[2:]) * 1j

    # distance between the sensor and beacon
    offset = sensor - beacon
    distance = max(int(abs(offset.real) + abs(offset.imag)))
    
    # how much of the row is blocked off? it's (2*exclu + 1) units, centred on sx
    exclu = distance - abs(ROW_TO_CHECK - sensor.imag)

    # print(sensor, beacon)
    # print(f"at row {ROW_TO_CHECK}, the exclusion zone is of size {exclu}, hence range from {int(sensor.real - exclu)} to {int(sensor.real - exclu)} inclusive")

    # a range of (2*exclu + 1) units, centred on sx (unless this is negative)
    if exclu >= 0:
        excluded.append(range(int(sensor.real - exclu), int(sensor.real + exclu + 1)))

# start and end points of ranges
starts = map(lambda x: x.start, excluded)
ends = map(lambda x: x.stop, excluded)

# the furthest left and right bit that's in our answer 
print(a := min(starts), b := max(ends) - 1)

# our answer
print(sum(any((i in r for r in excluded)) for i in range(a, b)))

