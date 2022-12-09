import aoc.utility as util

commandMap = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def main():
    year = 2022
    day = 9
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    commandList = data.splitlines()
    print(commandList)

    gridMap = {}
    headCoordinate = (0, 0)
    tailCoordinate = headCoordinate

    gridMap[headCoordinate] = "#"

    for command in commandList:
        direction, step = command.rsplit(" ")
        stepX, stepY = commandMap[direction]
        for i in range(int(step)):
            headCoordinate = (headCoordinate[0] + stepX, headCoordinate[1] + stepY)
            tailCoordinate = getNewTailCoordinate(headCoordinate, tailCoordinate)
            gridMap[tailCoordinate] = "#"

            # print(f"head={headCoordinate}, tail={tailCoordinate}")

    # printGrid(gridMap)
    return len([value for value in gridMap.values() if value == "#"])


def getNewTailCoordinate(headCoordinate, tailCoordinate):
    diffX = headCoordinate[0] - tailCoordinate[0]
    diffY = headCoordinate[1] - tailCoordinate[1]
    if (abs(diffX) > 1 and abs(diffY) > 1):
        return (headCoordinate[0] - (1 if diffX > 0 else -1), headCoordinate[1] - (1 if diffY > 0 else -1))
    elif (abs(diffX) > 1):
        return (headCoordinate[0] - (1 if diffX > 0 else -1), headCoordinate[1])
    elif (abs(diffY) > 1):
        return (headCoordinate[0], headCoordinate[1] - (1 if diffY > 0 else -1))
    return tailCoordinate


def getAnsPart2(data):
    commandList = data.splitlines()
    print(commandList)
    gridMap = {}
    ropeCoordinates = [(0, 0)] * 10

    gridMap[ropeCoordinates[-1]] = "#"

    for command in commandList:
        direction, step = command.rsplit(" ")
        stepX, stepY = commandMap[direction]
        for i in range(int(step)):
            headCoordinate = ropeCoordinates[0]
            headCoordinate = (headCoordinate[0] + stepX, headCoordinate[1] + stepY)
            ropeCoordinates[0] = headCoordinate

            for i in range(len(ropeCoordinates)-1):
                ropeCoordinates[i+1] = getNewTailCoordinate(ropeCoordinates[i], ropeCoordinates[i+1])

            gridMap[ropeCoordinates[-1]] = "#"

    # printGrid(gridMap)
    return len([value for value in gridMap.values() if value == "#"])


def printGrid(gridMap):
    list(gridMap.keys())
    print(gridMap.keys())
    minX = min([key[0] for key in gridMap.keys()])
    maxX = max([key[0] for key in gridMap.keys()])
    minY = min([key[1] for key in gridMap.keys()])
    maxY = max([key[1] for key in gridMap.keys()])

    print(f"{minX}-{maxX}, {minY}-{maxY}")

    for y in range(minY, maxY)[::-1]:
        for x in range(minX, maxX):
            coordinate = (x, y)
            if (coordinate in gridMap):
                print(gridMap[coordinate], end="")
            else:
                print(".", end="")
        print()


main()
