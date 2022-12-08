import aoc.utility as util
from collections import Counter


def main():
    year = 2022
    day = 6
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    for i in range(4, len(data)):
        str = data[i-4:i]
        print(f"{i} : {str}")
        countList = [count for letter, count in Counter(str).items()]
        if max(countList) == 1:
            return i


def getAnsPart2(data):
    for i in range(14, len(data)):
        str = data[i-14:i]
        print(f"{i} : {str}")
        countList = [count for letter, count in Counter(str).items()]
        if max(countList) == 1:
            return i


main()
