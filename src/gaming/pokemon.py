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

if __name__ == "__main__":
    names, types = parseTypes("./src/gaming/types.txt")
    print(TypeChart(names, types))
