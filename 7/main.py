import adventofcode2022.aoc.utility as util

class Item:
    def __init__(self, name, size, type, items):
        self.name = name
        self.size = size
        self.type = type
        self.items = items

    def __str__(self):
        return f" {self.name}({self.type}) {self.size} : {self.items if self.items != None else None}"

    def __repr__(self):
        return f"{self.__str__()}"


def main():
    year = 2022
    day = 7
    local = 0
    util.mainProcess(year, day, local, getAnsPart1, getAnsPart2)


def getTotalSize(files):
    return sum([file[0] for file in files.values()])


def buildLinesFrom(data):
    lines = data.split("\n")
    lines = [item for item in lines if item != "$ ls" and item != "$ cd .."]
    return lines


def buildItemsFrom(lines):
    items = []
    accumulateItems = []
    for line in lines[::-1]:
        if line.startswith("$ cd"):
            accumulateItemFileSize = sum(
                [accumulateItem.size for accumulateItem in accumulateItems])
            folderName = line.split()[-1]
            items.append(
                Item(folderName, accumulateItemFileSize, "dir", accumulateItems)
            )
            accumulateItems = []
        elif line.startswith("dir"):
            folderName = line.split()[-1]
            seenFolder = [
                item for item in items if item.name == folderName][-1]
            accumulateItems.append(seenFolder)
            items.remove(seenFolder)
        else:
            fileSize, fileName = line.split()
            accumulateItems.append(
                Item(fileName, int(fileSize), "file", None)
            )
    return items


def getAnsPart1(data):
    items = buildItemsFrom(buildLinesFrom(data))

    rootItem = items[0]
    maximumFolderSize = 100000
    print(f"{rootItem.name} : {rootItem.size}")

    return (rootItem.size if rootItem.size <= maximumFolderSize else 0) + sumFolderSizeLessThanMaxSize(
        maximumFolderSize, rootItem.items)


def getAnsPart2(data):
    items = buildItemsFrom(buildLinesFrom(data))

    rootItem = items[0]
    print(f"{rootItem.name} : {rootItem.size}")
    sizeRequiredtoRemove = 3e7 - (7e7 - rootItem.size)
    print(f"require : {sizeRequiredtoRemove}")
    return findMinimumFileSizeToRemoveBySizeRequired(sizeRequiredtoRemove, rootItem.size, rootItem.items)


def sumFolderSizeLessThanMaxSize(maxFileSize, files):
    sumOfFileSize = 0
    for file in files:
        if (file.type == "file"):
            continue
        print(f"{file.name}({file.type}) : {file.size}")
        if (file.size <= maxFileSize):
            sumOfFileSize += file.size
        sumOfFileSize += sumFolderSizeLessThanMaxSize(
            maxFileSize, file.items)
    return sumOfFileSize


def findMinimumFileSizeToRemoveBySizeRequired(sizeRequiredtoRemove, minimumFileSize, files):
    for file in files:
        if (file.type == "file"):
            continue
        print(f"{file.name}({file.type}) : {file.size}")
        if (file.size < sizeRequiredtoRemove):
            continue
        elif (file.size == sizeRequiredtoRemove):
            return file.size
        elif (file.size > sizeRequiredtoRemove and file.size < minimumFileSize):
            minimumFileSize = findMinimumFileSizeToRemoveBySizeRequired(
                sizeRequiredtoRemove, file.size, file.items)
    return minimumFileSize


main()
