import aoc.utility as util


def main():
    year = 2022
    day = 3
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    sum = 0
    dataList = data.split("\n")
    dataListSplit = [[item[:len(item)//2], item[len(item)//2:]]
                     for item in dataList]
    print(dataListSplit)
    for item in dataListSplit:
        print(f"===={item}====")
        for char in item[0]:
            if (char in item[1]):
                sum += getCharValue(char)
                break
    return sum


def getAnsPart2(data):
    sum = 0
    n = 3
    dataList = data.split("\n")
    list_of_groups = [dataList[i:i+n] for i in range(0, len(dataList), n)]
    print(list_of_groups)
    for group in list_of_groups:
        print(f"===={group}====")
        for char in group[0]:
            if (char in group[1] and char in group[2]):
                sum += getCharValue(char)
                break
    return sum


def getCharValue(char):
    if char.islower():
        value = ord(char) - 96
    else:
        value = ord(char) - 64 + 26
    print("{}:{}".format(char, value))
    return value


main()
