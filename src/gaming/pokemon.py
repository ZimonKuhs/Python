"""
    Do stuff with those stuffs.

    @author Zimon Kuhs
    @date   2021-11-14
"""

import random
import os
import sys
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


class Table:

    def __init__(self):
        table = {}


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

def countMoves(filePath):
    lines = []

    with open(filePath, encoding="utf-8") as contents:
        lines = contents.readlines()

    moves = {}
    for line in lines:
        if not line:
            continue

        parts = line.split()
        for part in parts:
            moves[part] = 1 if part not in moves else moves[part] + 1

    sortedMoves = sorted(moves.items(), key = lambda arg: arg[1], reverse = True)
    moves.clear()
    for pair in sortedMoves:
        moves[pair[0]] = pair[1]

    return moves

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
    names = ["HP", "ATK", "DEF", "SPD", "SPC"]
    #stats = estimateStatExp([40, 40, 35, 70, 100], 10, [31, 16, 15, 23, 28], [15, 15, 15, 15, 15])
    tentacool = calculateStats([40, 40, 35, 70, 100], 7, dvs=[15, 15, 15, 15, 15])
    tentacruel = calculateStats([80, 70, 65, 100, 120], 7, dvs=[15, 15, 15, 15, 15])

    for index in range(5):
        print(f"{names[index]}: {tentacruel[index] - tentacool[index]}")

    #for move, amount in countMoves("src/gaming/euphoricMoves.txt").items():
    #    print(f"{move}: {amount}")

