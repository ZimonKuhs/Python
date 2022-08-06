"""
    Do stuff with those stuffs.

    @author Zimon Kuhs
    @date   2021-11-14
"""

import functools
import os
from random import randint
import sys

from iniconfig import ParseError

class Pokemon:

    def __init__(self, number, name, health, attack, defense, speed, special, level = 1):
        self.number     = int(number)
        self.name       = str(name)
        self.health     = int(health)
        self.attack     = int(attack)
        self.defense    = int(defense)
        self.speed      = int(speed)
        self.special    = int(special)
        self.level      = int(level)

    def criticalChance(self, highCrit=False):
        return round(100 * min ((8 if highCrit else 1) * self.speed / 2, 255) / 256, 2)


class Finisher:

    def __init__(self, name, time, level, moves, stats):
        self.species    = str(name)
        self.health     = int(stats[0])
        self.attack     = int(stats[1])
        self.defense    = int(stats[2])
        self.speed      = int(stats[3])
        self.special    = int(stats[4])
        self.lvl        = int(level)
        self.myMoves    = [str(move) for move in moves]

        finish = time.split(":")
        self.hour, self.min = int(finish[0]), int(finish[1])

    def name(self):
        return self.species

    def level(self):
        return self.lvl

    def moves(self):
        return [move for move in self.myMoves]

    def minutes(self):
        return self.hour * 60 + self.min


def compareMoves(move1, move2):
    count = move2[1] - move1[1]
    if count != 0:
        return count

    cmp = 0
    word1, word2 = move1[0], move2[0]
    for index in range(min(len(word1), len(word2))):
        cmp = ord(word1[index]) - ord(word2[index])

        if cmp != 0:
            return cmp

    return 0


class Euphoria:

    def __init__(self):
        self.table = {}
        self.fast = None
        self.high = None
        self.low  = None
        self.slow = None


    def add(self, name, order, time, level, moves, stats):
        finisher = Finisher(name, time, level, moves, stats)
        self.table[int(order)] = finisher

        if len(self.table) <= 1:
            self.fast = self.high = self.low = self.slow = finisher
            return

        duration = finisher.minutes()
        if duration < self.fast.minutes():
            self.fast = finisher
        elif duration > self.slow.minutes():
            self.slow = finisher

        lvl = int(level)
        if lvl < self.low.level():
            self.low = finisher
        elif lvl > self.high.level():
            self.high = finisher

    def countMoves(self):
        result = {}
        for _, pokemon in self.table.items():
            for move in pokemon.moves():
                result[move] = 1 + result[move] if move in result else 1

        return {key: value for key, value in sorted(result.items(), key = functools.cmp_to_key(compareMoves))}

    def fastest(self):
        return self.fast

    def highest(self):
        return self.high

    def lowest(self):
        return self.low

    def slowest(self):
        return self.slow

    def names(self):
        result = [pokemon.name() for _, pokemon in self.table.items()]
        result.sort()
        return result


def error(message, code=1):
    if code <= 0:
        raise ValueError(f"Error codes must be positive integers, got {code}")

    print(message)
    sys.exit(code)


def parsePokemon(line):
    data = line.split()

    # Mr. Mime...
    if len(data) == 12:
        data[1] = data[1] + data.pop(2)
        data[2] = data[2] + data.pop(3)

    return Pokemon(data[0], data[1], data[3], data[4], data[5], data[6], data[7])

def replace(string, replacements):
    if not len(string):
        return string

    for switch in replacements:
        string = string.replace(switch[0], switch[1])

    return string

def parseTypes(typeFile):
    lines = []
    replacements = [["x", ""], ["X", ""], ["1/2", "0.5"]]

    with open(typeFile, encoding="utf-8") as contents:
        lines = contents.readlines()

    names = lines.pop(0).split()
    lines = [line.split()[1:] for line in [replace(string, replacements) for string in lines]]

    matrix = []
    for line in lines:
        matrix.append([float(number) for number in line])

    return names, matrix

def fromRawToStats(rawPath, outputPath):
    if os.path.exists(outputPath):
        raise FileExistsError(outputPath)

    pokemon = {}
    with open(rawPath, encoding="utf-8") as rawStats:
        for line in rawStats.readlines():
            monster = parsePokemon(line)
            pokemon[monster.number] = monster

    with open(outputPath, "w", encoding="utf-8") as statFile:
        lines = []
        for _, monster in pokemon.items():
            lines.append(f"{monster.number} {monster.name} {monster.health} {monster.attack} " +
                         f"{monster.defense} {monster.speed} {monster.special}\n")

        statFile.writelines(lines)

def averageEncounterLevel(filePath):
    lines = []

    with open(filePath, encoding="utf-8") as contents:
        lines = contents.readlines()

    ratio = [int(number) for number in lines.pop(0).split()]
    print(len(ratio))

    amounts = {}
    rates = {}
    for line in lines:
        parts = line.split()
        name = parts.pop(0)
        numbers = [int(part[1:]) for part in parts if part[1:].isdigit()]

        rates[name] = rates[name] if name in rates else 0
        amounts[name] = amounts[name] if name in amounts else 0
        rates[name] += sum([ratio[index] * numbers[index] for index in range(0, len(ratio))]) / len(ratio)
        amounts[name] += 1

    result = {}
    for key, value in rates.items():
        result[key] = round(rates[key] / amounts[key])

    return sorted(result.items(), key = lambda arg: arg[1], reverse = True)

def skipLine(line):
    if line.lstrip()[0] == '#':
        return True

    count = 0
    parts = line.split(",")
    for part in parts:
        if not part:
            count += 1

        if count > 3:
            return True

    return False

def parseEuphoria(filePath):
    """
        Column 0:       Name
        Column 1:       Order
        Column 2:       Space
        Column 3:       Time
        Column 4:       Level
        Column 5:       Space
        Column 6-9:     Moves
        Column 10       Space
        Column 11-15:   Stats
    """

    lines = []

    with open(filePath, encoding="utf-8") as contents:
        lines = contents.readlines()

    expected = 16
    lineNumber = 0
    results = Euphoria()

    for line in lines:
        lineNumber += 1

        if lineNumber < 2 or not line or skipLine(line):
            continue

        parts = line.split(",")

        if len(parts) != expected:
            raise ParseError(f"Invalid format of line {lineNumber} (expected {expected} commas):\"\n\t{line}\n")

        results.add(parts[0], parts[1], parts[3], parts[4], parts[6:10], parts[11:16])

    return results

def statExp(base, level, stat, dv, hp = False):
    const = level + 10 if hp else 5
    return pow(8 * ((50 / level) * (stat - const) - base - dv), 2)

def estimateStatExp(baseStats, level, stats, dvs=[0, 0, 0, 0, 0]):
    lenBase, lenStats, lenDVs = len(baseStats), len(stats), len(dvs)

    if lenBase != lenDVs or lenBase != lenStats:
        raise ValueError(f"Amount of base stats, stats, and DVs are different! ({lenBase}, {lenStats}, {lenDVs})")

    hp = True
    result = []
    for index in range(lenBase):
        result.append(statExp(baseStats[index], level, stats[index], dvs[index], hp))
        hp = False

    return result

def calculateStats(baseStats, level, dvs=[0, 0, 0, 0, 0]):
    lenBase, lenDVs = len(baseStats), len(dvs)

    if lenBase != lenDVs:
        raise ValueError(f"Amount of stats different from amount of DVs! ({lenBase} and {lenDVs})")

    result = []
    for index in range(lenBase):
        result.append(int(2 * level * (baseStats[index] + dvs[index]) / 100 + 5))
    result[0] += level + 5

    return result


def burpTypeEnum():
    string = "NONE,BUG,DRAGON,ELECTRIC,FIGHTING,FIRE,FLYING,GHOST,GRASS,GROUND,ICE,NORMAL,POISON,PSYCHIC,ROCK,WATER"

    parts = string.split(",")
    print("{")
    for part in parts:
        print(f"    {{ \"{part}\", {part} }},")
    print("};")
    return True

def pad(string, length):
    return string + " " * max(length - len(string), 0)

def burpNameListEnum():
    string = "NONE,BUG,DRAGON,ELECTRIC,FIGHTING,FIRE,FLYING,GHOST,GRASS,GROUND,ICE,NORMAL,POISON,PSYCHIC,ROCK,WATER"

    parts = string.split(",")
    length = max([len(part) for part in parts])

    for part in parts:
        print(f"{pad(part, length)} = Type(\"{part}\")")

    return True

def nextChallenge(filePath):
    lines = None
    with open(csvFile, "r", encoding="utf-8") as content:
        lines = content.readlines()

    names = []
    for line in lines:
        parts = line.split(",")

        if parts[1]:
            continue

        names.append(parts[0])

    return names[randint(0, len(names))]

if __name__ == "__main__":

    arg = sys.argv[1]
    csvFile = "src/gaming/data/Euphoria results - Sheet1.csv"

    if arg == "--records":
        euphoria = parseEuphoria(csvFile)

        print(f"Low:  {euphoria.lowest().name()}")
        print(f"High: {euphoria.highest().name()}")
        print(f"Fast: {euphoria.fastest().name()}")
        print(f"Slow: {euphoria.slowest().name()}")

    elif arg == "--moveCount":
        counts = parseEuphoria(csvFile).countMoves()
        chars = max([len(move) for move, _ in counts.items()])

        for move, amount in counts.items():
            padding = " " * (chars - len(move) + 5)
            print(f"{move}{padding}{amount}")

    elif arg == "--next":
        print(nextChallenge(csvFile))

    elif arg == "--finishers":
        for mon in parseEuphoria(csvFile).names():
            print(mon)

    elif arg == "--types":
        import typeChart
        results = {}

        for mon in parseEuphoria(csvFile).names():
            types = typeChart.getTypes(mon)
            typeName = (types[0]).name()
            results[typeName] = 1 if typeName not in results else results[typeName] + 1

            if types[1] is not typeChart.NONE:
                typeName = types[1].name()
                results[typeName] = 1 if typeName not in results else results[typeName] + 1

        for name, _ in typeChart.types.items():
            if name not in results and name != "NONE":
                results[name] = 0

        sorted = {}
        keys = [key for key in results.keys()]
        keys.sort()

        for key in keys:
            sorted[key] = results[key]

        for name, amount in sorted.items():
            padding = " " * (len(typeChart.ELECTRIC.name()) - len(name) + 1)
            print(f"{name}:{padding}{amount}")
