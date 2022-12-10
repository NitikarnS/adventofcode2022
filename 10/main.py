import aoc.utility as util


def main():
    year = 2022
    day = 10
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    signal = [20, 60, 100, 140, 180, 220]

    instList = data.split("\n")
    newInstList = []
    [newInstList.append(inst) if (inst == "noop") else newInstList.extend(["noop", inst]) for inst in instList]

    print(newInstList)

    sum = 0
    X = 1
    for i, inst in enumerate(newInstList):
        cycle = i + 1
        if (cycle in signal):
            sum += X * cycle
        if (inst != "noop"):
            X += int(inst.split(" ")[-1])
    return sum


def getAnsPart2(data):
    spriteMark = 0

    instList = data.split("\n")
    newInstList = []
    [newInstList.append(inst) if (inst == "noop") else newInstList.extend(["noop", inst]) for inst in instList]

    crt = ""
    for i, inst in enumerate(newInstList): 
        if ((i)%40 in range(spriteMark, spriteMark + 3)):
            crt += ("#")
        else:
            crt += (".")
        if (inst != "noop"):
            value = int(inst.split(" ")[-1])
            spriteMark = spriteMark + value
            
        if ((i+1) % 40 == 0):
            print(crt)
            crt = ""

main()
