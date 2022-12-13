import aoc.utility as util
from functools import cmp_to_key


def main():
    year = 2022
    day = 13
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    pairs = data.split("\n\n")
    pairs = [packets.split("\n") for packets in pairs]
    print(pairs)
    _sum = 0
    for i, packets in enumerate(pairs):
        index = i+1
        list1 = eval(packets[0])
        list2 = eval(packets[1])
        print(list1)
        print(list2)
        if (verifyPackets(list1, list2)):
            print("right order")
            _sum += index
        print("=========")
    return _sum

def verifyPackets(list1, list2):
    l1 = [item for item in list1]
    l2 = [item for item in list2]
    if len(l1) < len(l2):
        l1.extend([None] * (len(l2) - len(l1)))
    else:
        l2.extend([None] * (len(l1) - len(l2)))
    for i1, i2 in zip(l1, l2):
        if (i1 is None and i2 is not None):
            return True
        elif (i1 is not None and i2 is None):
            return False
        elif (type(i1) is list and type(i2) is not list):
            res = verifyPackets(i1, [i2])
            if (res is not None):
                return res
        elif (type(i1) is not list and type(i2) is list):
            res = verifyPackets([i1], i2)
            if (res is not None):
                return res
        elif (type(i1) is list and type(i2) is list):
            res = verifyPackets(i1, i2)
            if (res is not None):
                return res
        elif (i1 != i2):
            return i1 < i2


def getAnsPart2(data):
    packets = [eval(packet) for packet in data.split("\n") if packet is not ""]
    print(packets)
    packets.extend([[[2]], [[6]]])
    packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    print(packets)
    index1 = packets.index([[2]]) + 1
    index2 = packets.index([[6]]) + 1
    return index1 * index2

def compare(list1, list2):
    res = verifyPackets(list1, list2)
    if res == None:
        return 0
    return 1 if res else -1

main()
