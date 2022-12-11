import aoc.utility as util
from functools import reduce
from math import lcm

class Monkey:
    def __init__(self, items, oper, divider, path1, path2):
        self.items = items
        self.oper = oper.strip()
        self.divider = divider
        self.path1 = path1
        self.path2 = path2
        self.inspect = 0

    def __str__(self):
        return f"Monkey({self.items}, {self.oper}, {self.divider}, ({self.path1}:{self.path2}))"


def main():
    year = 2022
    day = 11
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getAnsPart1(data):

    monkeys = {}

    inputs = [monkey.split("\n") for monkey in data.split("\n\n")]
    print(inputs)
    for id, input in enumerate(inputs):
        items = input[1].split(":")[-1]
        oper = input[2].split("=")[-1]
        divider = int(input[3].split(" ")[-1])
        path1 = int(input[4].split(" ")[-1])
        path2 = int(input[5].split(" ")[-1])
        print(items)
        monkeys[id] = (Monkey(eval(f"[{items}]"), oper, divider, path1, path2))
        # print(monkeys)
    [print(monkey) for monkey in monkeys.values()]

    for i in range(20):
        for monkey in monkeys.values():
            for item in monkey.items:
                old = item
                new = eval(monkey.oper) // 3
                # print(f"new: {new}")
                if (new % monkey.divider == 0):
                    monkeys[monkey.path1].items.append(new)
                else:
                    monkeys[monkey.path2].items.append(new)
                monkey.inspect += 1
            monkey.items = []
        print(",".join([str(monkey.inspect) for monkey in monkeys.values()]))

    inspects = [monkey.inspect for monkey in monkeys.values()]
    inspects.sort()
    return reduce((lambda x, y: x * y), inspects[-2:])

def getAnsPart2(data):
    monkeys = {}

    inputs = [monkey.split("\n") for monkey in data.split("\n\n")]
    print(inputs)
    for id, input in enumerate(inputs):
        items = input[1].split(":")[-1]
        oper = input[2].split("=")[-1]
        divider = int(input[3].split(" ")[-1])
        path1 = int(input[4].split(" ")[-1])
        path2 = int(input[5].split(" ")[-1])
        print(items)
        monkeys[id] = (Monkey(eval(f"[{items}]"), oper, divider, path1, path2))
        # print(monkeys)
    [print(monkey) for monkey in monkeys.values()]

    lcmValue = lcm(*[monkey.divider for monkey in monkeys.values()])
    print(f"{lcmValue} of {[monkey.divider for monkey in monkeys.values()]}")

    for i in range(10000):
        for monkey in monkeys.values():
            for item in monkey.items:
                old = item
                new = (eval(monkey.oper)) % lcmValue
                # print(f"new: {new}")
                if (new % monkey.divider == 0):
                    monkeys[monkey.path1].items.append(new)
                else:
                    monkeys[monkey.path2].items.append(new)
                monkey.inspect += 1
            monkey.items = []
        print(f"round {i+1} :"+",".join([str(monkey.inspect) for monkey in monkeys.values()]))

    print([monkey.items for monkey in monkeys.values()])
    inspects = [monkey.inspect for monkey in monkeys.values()]
    inspects.sort()
    return reduce((lambda x, y: x * y), inspects[-2:])


main()
