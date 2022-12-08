import aoc.utility as util


def main():
    year = 2022
    day = 4
    local = 1
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    dataList = data.split("\n")
    print(dataList)
    assignList = [[[int(floor) for floor in pair.split("-")] for pair in assign.split(",")]
                  for assign in dataList]
    print(assignList)
    contain = 0
    for pair in assignList:
        if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            # print(pair)
            contain += 1
        elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            # print(pair)
            contain += 1

    return contain


def getAnsPart2(data):
    dataList = data.split("\n")
    print(dataList)
    assignList = [[[int(floor) for floor in pair.split("-")] for pair in assign.split(",")]
                  for assign in dataList]
    print(assignList)
    overlap = 0
    for pair in assignList:
        if pair[0][0] in range(pair[1][0], pair[1][1]+1) or pair[0][1] in range(pair[1][0], pair[1][1]+1):
            print(pair)
            overlap += 1
        elif pair[1][0] in range(pair[0][0], pair[0][1]+1) or pair[1][1] in range(pair[0][0], pair[0][1]+1):
            print(pair)
            overlap += 1

    return overlap


main()
