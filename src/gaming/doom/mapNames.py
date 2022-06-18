import os
import sys

def parseMapName(string):
    parts = string.split()
    if len(parts) < 2:
        raise ValueError(f"Invalid line found: {string}")

    middle = ""
    name = ""

    for part in parts[1:]:
        if part == "by":
            break

        name = f"{name}{middle}{part}"
        middle = " "

    return name

# # # #

fileName = sys.argv[1]
lines = []

with open(f"src/gaming/doom/data/{fileName}", "r", encoding="utf-8") as contents:
    lines = contents.readlines()

result = []
for line in lines:
    text = line.strip()
    if not text or text.startswith("#"):
        continue

    result.append(parseMapName(text))

for res in result:
    print(res)
