import aoc.utility as util


def main():
    year = 2022
    day = 14
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    wallMap = {}
    data = data.split("\n")
    data = [line.split("->") for line in data]
    for line in data:
        for i in range(len(line)-1):
            x, y = zip(eval(line[i]), eval(line[i+1]))
            rx = range(min(x), 1 + min(x) + abs(x[0] - x[1]))
            ry = range(min(y), 1 + min(y) + abs(y[0] - y[1]))
            for _x in rx:
                for _y in ry:
                    wallMap[(_x, _y)] = "#"
    start = (500, 0)
    count = 0
    current = start
    while True:
        r = [p[1] for p in wallMap if (p[0] == current[0] and p[1] > current[1])]
        if (r):
            minR = min(r)
            current = (current[0], minR-1)
        else:
            break

        nexts = [(current[0], current[1]+1), (current[0]-1, current[1]+1), (current[0]+1, current[1]+1)]
        nexts = [next for next in nexts if next not in wallMap.keys()]
        if (nexts):
            current = nexts[0]
        else:
            wallMap[current] = "O"
            count += 1
            current = (500, 0)
    return count


def printWall(wallMap):
    print("=======")
    _x = [point[0] for point in wallMap]
    minX, maxX = min(_x), max(_x)
    _y = [point[1] for point in wallMap]
    maxY = max(_y)
    for h in range(maxY+1):
        for w in range(minX, maxX+1):
            if ((w, h) in wallMap.keys()):
                print(wallMap[(w, h)], end="")
            else:
                print(".", end="")
        print()


def getAnsPart2(data):
    wallMap = {}
    data = data.split("\n")
    data = [line.split("->") for line in data]
    maxY = 0
    for line in data:
        for i in range(len(line)-1):
            x, y = zip(eval(line[i]), eval(line[i+1]))
            # print(x, y)
            rx = range(min(x), 1 + min(x) + abs(x[0] - x[1]))
            ry = range(min(y), 1 + min(y) + abs(y[0] - y[1]))
            for _x in rx:
                for _y in ry:
                    maxY = _y if _y > maxY else maxY
                    wallMap[(_x, _y)] = "#"
    maxY += 2
    initPoint = [(500, 0)]
    count = 0
    while True:
        print(initPoint)
        nexts = set()
        for current in initPoint:
            wallMap[current] = "O"
            count += 1

            next = [(current[0], current[1]+1), (current[0]-1, current[1]+1), (current[0]+1, current[1]+1)]
            next = [point for point in next if point not in wallMap.keys()]
            nexts.update(next)
        if (current[1]+1 == maxY):
            break
        initPoint = list(nexts)

    return count


main()
