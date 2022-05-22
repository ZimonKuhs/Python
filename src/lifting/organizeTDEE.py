import os

file = "src/lifting/data/tdeeData.txt"

if not os.path.exists(file):
    raise FileNotFoundError(file)

lines = []
with open(file) as contents:
    lines = contents.readlines()

data = {}
for index in range(len(lines) - 1, -1, -1):
    line = lines[index]
    parts = line.split(" ")

    if (len(parts) != 3):
        raise ValueError(f"Invalid line {line}")

    data[parts[0]] = (float(parts[1]), int(parts[2]))

print("-----------------------------")
amount = 0
prefix = ""
kcals = ""
weights = ""
for key, value in data.items():
    if amount == 7:
        print(weights)
        print(kcals)
        kcals = ""
        weights = ""
        prefix = ""
        amount = 0
    amount += 1
    weights += prefix + f"{value[0]}"
    kcals += prefix + f"{value[1]}"
    prefix = " "
print("-----------------------------")
