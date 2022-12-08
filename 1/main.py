import aoc.utility as util


def main():
    year = 2022
    day = 1
    local = 1
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    listSum = findSumGroup(data.split("\n"))
    return max(listSum)


def getAnsPart2(data):
    listSum = findSumGroup(data.split("\n"))
    max1 = max(listSum)
    listSum.remove(max1)
    max2 = max(listSum)
    listSum.remove(max2)
    max3 = max(listSum)
    return max1+max2+max3


def findSumGroup(list):
    if "" in list:
        indexEmpty = list.index("")
        sumOfFirstGroup = sum([int(item) for item in list[:indexEmpty]])
    else:
        return [sum([int(item) for item in list])]
    listSum = [sumOfFirstGroup]
    listSum.extend(findSumGroup(list[indexEmpty+1:]))
    return listSum


main()
