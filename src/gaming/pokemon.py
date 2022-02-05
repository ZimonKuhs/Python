"""
    Do stuff with those stuffs.

    @author Zimon Kuhs
    @date   2021-11-14
"""

import functools
import os
import sys

from iniconfig import ParseError
from typeChart import TypeChart

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
        self.name       = str(name)
        self.health     = int(stats[0])
        self.attack     = int(stats[1])
        self.defense    = int(stats[2])
        self.speed      = int(stats[3])
        self.special    = int(stats[4])
        self.level      = int(level)
        self.myMoves    = [str(move) for move in moves]

        finish = time.split(":")
        self.hours, self.minutes = int(finish[0]), int(finish[1])

    def moves(self):
        return [move for move in self.myMoves]


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

    def add(self, name, order, time, level, moves, stats):
        self.table[int(order)] = Finisher(name, time, level, moves, stats)

    def countMoves(self):
        result = {}
        for _, pokemon in self.table.items():
            for move in pokemon.moves():
                result[move] = 1 + result[move] if move in result else 1

        return {key: value for key, value in sorted(result.items(), key = functools.cmp_to_key(compareMoves))}


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

        if lineNumber < 3 or not line or skipLine(line):
            continue

        parts = line.split(",")

        if len(parts) != expected:
            raise ParseError(f"Invalid format of line {lineNumber} (expected {expected} commas):\"\n\t{line}\n")

        for part in parts:
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


if __name__ == "__main__":
    for move, amount in parseEuphoria("src/gaming/data/Euphoria results - Sheet1.csv").countMoves().items():
        print(f"{move}: {amount}")

