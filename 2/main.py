import aoc.utility as util

valueMap = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def main():
    year = 2022
    day = 2
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):
    rounds = data.split("\n")
    print(rounds)
    rounds = [item.split() for item in rounds]
    print(rounds)
    rounds = [[valueMap[value] for value in item] for item in rounds]
    print(rounds)
    score = 0
    for round in rounds:
        if round[0] == round[1]:
            score += round[1] + 3
        elif round[0] + 1 == round[1] or round[0] - 2 == round[1]:
            score += round[1] + 6
        else:
            score += round[1]
    return score


def getAnsPart2(data):
    rounds = data.split("\n")
    print(rounds)
    rounds = [item.split() for item in rounds]
    print(rounds)
    rounds = [[valueMap[value] for value in item] for item in rounds]
    print(rounds)
    score = sum([getScoreByResult(value[0], value[1]) for value in rounds])
    return score


def getScoreByResult(value1, result):
    map = [1, 2, 3]
    scoreMap = {1: 0, 2: 3, 3: 6}
    if (result == 1):
        value2 = map[map.index(value1)-1]
    elif (result == 2):
        value2 = value1
    else:
        value2 = map[(map.index(value1)+1) % 3]
    print("{} vs {} = {}".format(value1, value2, result))
    return value2 + scoreMap[result]


main()
