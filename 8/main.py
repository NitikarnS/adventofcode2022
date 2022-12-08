import aoc.utility as util


def main():
    year = 2022
    day = 8
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    grid = data.split("\n")
    grid = [list(row) for row in grid]

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            col = row[j]
            print(col, end="")
        print()

    print()

    count = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            col = row[j]
            visible = False
            if (i == 0 or i == len(grid) - 1):
                visible = True
            elif (j == 0 or j == len(row) - 1):
                visible = True
            elif (max(row[:j]) < col):
                visible = True
            elif (max(row[j+1:]) < col):
                visible = True
            elif (max(getListTopFromGrid(grid, i, j)) < col):
                visible = True
            elif (max(getListBottomFromGrid(grid, i, j)) < col):
                visible = True

            if visible:
                print(col, end="")
                count += 1
            else:
                print(" ", end="")

        print()

    return count


def getListTopFromGrid(grid, y, x):
    list = []
    for i in range(len(grid)):
        if (i == y):
            break
        list.append(grid[i][x])
    return list


def getListBottomFromGrid(grid, y, x):
    list = []
    for i in range(y+1, len(grid)):
        list.append(grid[i][x])
    return list


def getAnsPart2(data):
    grid = data.split("\n")
    grid = [list(row) for row in grid]

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            col = row[j]
            print(col, end="")
        print()

    print()

    maxScore = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            col = row[j]
            if (i == 0 or i == len(grid) - 1) or (j == 0 or j == len(row) - 1):
                continue
            score = getListTopTreeFromGrid(grid, i, j) * getListBottomTreeFromGrid(grid, i, j) * getListLeftTreeFromGrid(grid, i, j) * getListRightTreeFromGrid(grid, i, j)
            if score > maxScore:
                maxScore = score 

    return maxScore

def getListTopTreeFromGrid(grid, y, x):
    count = 0
    for i in range(y)[::-1]:
        if (grid[i][x] >= grid[y][x]):
            count += 1
            break
        count += 1
    return count


def getListBottomTreeFromGrid(grid, y, x):
    count = 0
    for i in range(y+1, len(grid)):
        if (grid[i][x] >= grid[y][x]):
            count += 1
            break
        count += 1
    return count


def getListLeftTreeFromGrid(grid, y, x):
    count = 0
    for j in range(x)[::-1]:
        if (grid[y][j] >= grid[y][x]):
            count += 1
            break
        count += 1
    return count

def getListRightTreeFromGrid(grid, y, x):
    count = 0
    size = len(grid[0])
    for j in range(x+1, size):
        if (grid[y][j] >= grid[y][x]):
            count += 1
            break
        count += 1
    return count


main()