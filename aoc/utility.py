from aocd import get_data
from aocd import submit
import sys
import os.path
import json

# your session
session = "53616c7465645f5f15624a73ec8102b8db79787aae9427a3e27cd00591c992f7ac43f6d244198aad0671f3f598229e3c7d8b6620d47c46149de66100fe67c6a2"


def mainProcess(year, day, local, part1, part2):
    print("GET DATA DAY:{} FROM {}".format(
        day, "File" if local == 1 else "AOC-Data"))
    data = getData(year, day, local)
    print("RECEIVED DATA")
    print(data)

    print("====================")

    print("PART 1")
    ans1 = part1(data)
    print("END PART 1")

    print("====================")

    print("PART 2")
    ans2 = part2(data)
    print("END PART 2")

    print("====================")

    print("PART 1 : {}".format(ans1))
    print("PART 2 : {}".format(ans2))

    print("====================")

    if local == 0:
        if ans1 != None:
            print("SUBMIT RESULT PART A :")
            result1 = submitAnswer(year=year, day=day, part="a", answer=ans1)
            
        if ans2 != None:
            print("SUBMIT RESULT PART B :")
            result2 = submitAnswer(year=year, day=day, part="b", answer=ans2)


def getDataFromFile(day):
    scriptdir = sys.path[0]
    with open(os.path.join(scriptdir, 'input.txt')) as fl:
        file_contents = fl.read()
    return file_contents


def getData(year, day, custom):
    if (custom):
        return getDataFromFile(day)
    else:
        return get_data(session=session, day=day, year=year)


def submitAnswer(year, day, part, answer):
    return submit(answer, session=session, part=part, day=day, year=year)