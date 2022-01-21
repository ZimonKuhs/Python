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
