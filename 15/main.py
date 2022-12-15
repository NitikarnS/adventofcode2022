import aoc.utility as util
import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__str__()}"

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def __hash__(self):
        return hash(self.__str__())


def main():
    year = 2022
    day = 15
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    allMark = set()

    inputs = []
    for line in data.split("\n"):
        match = re.findall(r"x=(-?\d+), y=(-?\d+)", line)
        input = []
        for m in match:
            input.append(Point(int(m[0]), int(m[1])))
        inputs.append(input)
    print(inputs)

    y = 2000000
    _sb = []
    for input in inputs:
        if (input[0].y == y):
            _sb.append(input[0])
        if (input[1].y == y):
            _sb.append(input[1])
        _diff = abs(input[0].x - input[1].x) + abs(input[0].y - input[1].y)
        _diffToY = abs(input[0].y - y)
        if _diffToY > _diff:
            continue
        marks = []
        for i in range(_diff - _diffToY + 1):
            marks.append(Point(input[0].x+i, y))
            marks.append(Point(input[0].x-i, y))
        allMark.update(marks)
    allMark = [mark for mark in allMark if mark not in _sb]
    return len(allMark)


def getAnsPart2(data):
    inputs = []
    for line in data.split("\n"):
        match = re.findall(r"x=(-?\d+), y=(-?\d+)", line)
        input = []
        for m in match:
            input.append(Point(int(m[0]), int(m[1])))
        inputs.append(input)

    sbList = [[input[0], abs(input[0].x - input[1].x) + abs(input[0].y - input[1].y)] for input in inputs]
    dimention = 4000000
    x, y = 0, 0
    while True:
        print(x, y)
        inArea = False
        for sb in sbList:
            d = abs(sb[0].x - x) + abs(sb[0].y - y)
            if sb[1] >= d:
                inArea = True
                x = sb[0].x + (sb[1] - abs(sb[0].y - y))
                break
        if (not inArea):
            print(x, y)  # 3244277 2973564
            return x*4000000 + y
        if (x >= dimention):
            x, y = 0, y+1
        else:
            x += 1


def checkDistances(inputs, x, y):
    for input in inputs:
        d1 = abs(input[0].x - input[1].x) + abs(input[0].y - input[1].y)
        d2 = abs(input[0].x - x) + abs(input[0].y - y)
        if d1 >= d2:
            return False
    return True


def printSignal(signal):
    _x = [point.x for point in signal]
    minX, maxX = min(_x), max(_x)
    _y = [point.y for point in signal]
    minY, maxY = min(_y), max(_y)
    print(minX, maxX)
    print(minY, maxY)

    for x in range(minX, maxX+1):
        print(f"{x}".rjust(2), end="")
        for y in range(minY, maxY+1):
            if (Point(x, y) in signal):
                print("#", end="")
            else:
                print(".", end="")
        print()


main()
