class Type:
    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name

NONE     = Type("NONE")
BUG      = Type("BUG")
DRAGON   = Type("DRAGON")
ELECTRIC = Type("ELECTRIC")
FIGHTING = Type("FIGHTING")
FIRE     = Type("FIRE")
FLYING   = Type("FLYING")
GHOST    = Type("GHOST")
GRASS    = Type("GRASS")
GROUND   = Type("GROUND")
ICE      = Type("ICE")
NORMAL   = Type("NORMAL")
POISON   = Type("POISON")
PSYCHIC  = Type("PSYCHIC")
ROCK     = Type("ROCK")
WATER    = Type("WATER")

types = {
    { "NONE",     NONE },
    { "BUG",      BUG },
    { "DRAGON",   DRAGON },
    { "ELECTRIC", ELECTRIC },
    { "FIGHTING", FIGHTING },
    { "FIRE",     FIRE },
    { "FLYING",   FLYING },
    { "GHOST",    GHOST },
    { "GRASS",    GRASS },
    { "GROUND",   GROUND },
    { "ICE",      ICE },
    { "NORMAL",   NORMAL },
    { "POISON",   POISON },
    { "PSYCHIC",  PSYCHIC },
    { "ROCK",     ROCK },
    { "WATER",    WATER },
}

def equalizeLength(strings):
    result = []
    length = max([len(string) for string in strings])

    for string in strings:
        adjustment = length - len(string)

        if adjustment % 2 == 1:
            adjustment -= 1
            string = " " + string

        adjustment = int(adjustment / 2)

        result.append(" " * adjustment + string + " " * adjustment)

    return result, length

class TypeChart:

    def __init__(self, names, matrix):
        numberOfNames = len(names)
        numberOfTypes = len(matrix)

        if numberOfNames != numberOfTypes:
            raise ValueError("Name amount inconsistent with type amount.")

        for index in range(0, numberOfTypes):
            lineLength = len(matrix[index])

            if lineLength != numberOfTypes:
                raise ValueError(f"Matrix must be N x N; line {index} was {lineLength}, " +
                                 f"number of types is {numberOfTypes}")

        self.amount = numberOfTypes
        self.chart = matrix
        self.names = names

    def __str__(self):
        names, length = equalizeLength(self.names)
        string = "".join(names)

        return string

    def multiplier(self, attack, primary, secondary=None):
        print(self.chart[attack][primary])
