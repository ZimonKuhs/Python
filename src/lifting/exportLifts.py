def getExercise(nameParts):
    result = []
    for namePart in nameParts:
        if "(" in namePart:
            continue
        result.append(namePart.lower())

    return result

def highestPerDay():
    output = {}
    path = "D:\Code\Python\src\lifting\data\oldLifts_2.csv"
    out = f"{path.replace('.csv', '')}_3.csv"

    with open(path, "r", encoding="utf-8") as contents:
        for line in contents.readlines():
            parts = line.split()
            day = parts[0]
            name = " ".join(getExercise(parts[1:-2]))
            weight = parts[-2]
            reps = parts[-1]

            if not name:
                continue

            if name not in output:
                output[name] = {}
                output[name]["days"] = []
                output[name]["list"] = []

            if day not in output[name]["days"]:
                output[name]["days"].append(day)
                output[name]["list"].append({
                    "reps": reps,
                    "weight": weight,
                })

    keys = []
    for name in output.keys():
        keys.append(name)
    keys.sort()

    for key in keys:
        print(key)

    #with open(out, "w", encoding="utf-8") as contents:
    #    contents.writelines(output)

    return output


def removeRunning():
    path = "D:\Code\Python\src\lifting\data\oldLifts.csv"
    out = f"{path.replace('.csv', '')}_2.csv"

    with open(path, "r", encoding="utf-8") as contents:
        output = []
        for line in contents.readlines():
            if "km" not in line.split():
                output.append(line)

    with open(out, "w", encoding="utf-8") as contents:
        contents.writelines(output)

if __name__ == "__main__":
    test = ["a", "b", "c", "d", "e", "f", "g"]
    removeRunning()
    highestPerDay()
