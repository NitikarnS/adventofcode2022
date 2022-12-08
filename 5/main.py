import aoc.utility as util
from collections import deque


def main():
    year = 2022
    day = 5
    local = 1
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    dataList = data.split("\n")
    print(dataList)

    viewText = dataList[:dataList.index('')][::-1]
    comdText = dataList[dataList.index('')+1:]

    print(f"view: {viewText}")
    print(f"comd: {comdText}")

    stacks = createStacks(viewText)
    comdList = [[int(comd.split()[1]), int(comd.split()[3]),
                 int(comd.split()[5])] for comd in comdText]
    print(comdList)

    for comd in comdList:
        for i in range(comd[0]):
            stacks[comd[2] - 1].append(stacks[comd[1] - 1].pop())

    print(stacks)
    text = ""
    for stack in stacks:
        text += stack[-1]
    return text


def getAnsPart2(data):
    dataList = data.split("\n")
    print(dataList)

    viewText = dataList[:dataList.index('')][::-1]
    comdText = dataList[dataList.index('')+1:]

    print(f"view: {viewText}")
    print(f"comd: {comdText}")

    stacks = createStacks(viewText)
    comdList = [[int(comd.split()[1]), int(comd.split()[3]),
                 int(comd.split()[5])] for comd in comdText]
    print(comdList)

    for comd in comdList:
        temp = []
        for i in range(comd[0]):
            # print(f"{stacks[comd[1] - 1].pop()} - {stacks[comd[1] - 1]}")
            temp.append(stacks[comd[1] - 1].pop())
        stacks[comd[2] - 1].extend(temp[::-1])
        print(stacks)

    text = ""
    for stack in stacks:
        text += stack[-1]
    return text


def createStacks(views):
    views = deque(views)
    number = int(views.popleft()[-2])
    print(number)
    flow = [deque([]) for i in range(number)]
    print(flow)
    for line in views:
        pointer = 1
        for i in range(number):
            char = line[pointer]
            if char != ' ':
                flow[i].append(line[pointer])
            pointer += 4
    print(flow)
    return flow


main()
