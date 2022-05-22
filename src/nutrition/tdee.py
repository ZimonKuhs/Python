def parseLog(file):
    lines = None
    with open(file, "r", encoding="utf-8") as contents:
        lines = contents.readlines()

    weeks = []
    for index in range(len(lines) // 2):
        weightLine = lines[index * 2]
        kcalLine = lines[index * 2 + 1]

        weights = [float(number) for number in weightLine.split(",")]
        kcals = [int(number) for number in kcalLine.split(",")]
        weeks.append([(weights[index], kcals[index]) for index in range(0, len(weights))])

    return weeks


if __name__ == "__main__":

    data = parseLog("src/nutrition/data/log.csv")

    startWeek = 6
    for week in data:
        titleString = f"Week {startWeek}"
        print(f"{titleString}\n{'-' * len(titleString)}")
        for key, value in week:
            print(f"{key} = {value}")
        print()
        startWeek += 1

    avgs = []
    for week in data:
        size = len(week)
        avgKcal = 0
        avgWeight = 0.0

        for index in range(size):
            avgWeight += week[index][0]
            avgKcal += week[index][1]

        avgs.append((round(avgWeight / size, 1), avgKcal // size))

    print(avgs)

