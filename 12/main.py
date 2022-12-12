import aoc.utility as util


def main():
    year = 2022
    day = 12
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    grid = [[char for char in line] for line in data.split()]

    for i in range(len(grid)):
        if ("S" in grid[i]):
            start = (i, grid[i].index("S"))
        if ("E" in grid[i]):
            end = (i, grid[i].index("E"))
        for j in range(len(grid[i])):
            grid[i][j] = mapSignal(grid[i][j])

    pathMap = {}
    pathMap[start] = 0

    print(f"start: {start}")
    print(f"end: {end}")
    findRoute(grid=grid, pathMap=pathMap, curList=[start], step=1)

    return pathMap[end]


def findRoute(grid, pathMap, curList, step):
    if (len(curList) == 0):
        return
    nextPath = []
    for cur in curList:
        value = grid[cur[0]][cur[1]]
        allNextPath = findAllNextPath(grid, cur)
        for next in allNextPath:
            next_i, next_j = next[0], next[1]
            if (grid[next_i][next_j] in range(value+2)):
                if ((next_i, next_j) not in pathMap.keys() or pathMap[(next_i, next_j)] > step):
                    pathMap[(next_i, next_j)] = step
                    nextPath.append(next)

    findRoute(grid, pathMap, nextPath, step+1)


def findAllNextPath(grid, cur):
    current = cur
    allNextPath = []
    h = len(grid)
    w = len(grid[0])
    if (current[0] > 0):
        allNextPath.append((current[0]-1, current[1]))
    if (current[0] < h-1):
        allNextPath.append((current[0]+1, current[1]))
    if (current[1] > 0):
        allNextPath.append((current[0], current[1]-1))
    if (current[1] < w-1):
        allNextPath.append((current[0], current[1]+1))
    return allNextPath


def getAnsPart2(data):
    grid = [[char for char in line] for line in data.split()]

    startList = []
    for i in range(len(grid)):
        if ("E" in grid[i]):
            end = (i, grid[i].index("E"))
        for j in range(len(grid[i])):
            if (grid[i][j] in ("a", "S")):
                startList.append((i, j))
            grid[i][j] = mapSignal(grid[i][j])

    pathMap = {}

    for start in startList:
        pathMap[start] = 0

    findRoute(grid=grid, pathMap=pathMap, curList=startList, step=1)

    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if ((i, j) in pathMap.keys()):
    #             print(f"{pathMap[(i, j)]}".rjust(3), end="")
    #     print()

    return pathMap[end]


def mapSignal(signal):
    if signal == "S":
        return 1
    elif signal == "E":
        return 26
    return ord(signal) - 96


main()
