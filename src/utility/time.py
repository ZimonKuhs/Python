import sys

def addTime(*timestamps):
    inputTime = timestamps[0]

    parts = []
    for timestamp in inputTime:
        split = timestamp.split(":")
        if len(split) > 3:
            raise ValueError("Only seconds, minutes, and hours...")
        if len(split) < 3:
            split = [0] + split
        if len(split) < 2:
            split = [0] + split

        parts.append([int(time) for time in split])

    result = [0, 0, 0]
    for time in parts:
        for index in range(0, 3):
            result[index] += time[index]

    minutes, seconds = divmod(result[2], 60)
    hours, minutes = divmod(result[1] + minutes, 60)

    return hours + result[0], minutes, seconds


def divTime(time, divisor):
    if len(time) != 3:
        raise ValueError("Only HH:MM:SS")

    total = (time[0] * 60 + time[1]) * 60 + time[2]
    return round(total / divisor, 2)


if __name__ == "__main__":
    total = addTime(sys.argv[1:])
    print(divTime(total, (874 + 1519 + 1159)))
    print(f"{total[0]}:{total[1]}:{total[2]}")
