from random import randint
def test1():
    return 0

def distribution(attempts=100000, die=20, advantage=0):
    rolls = {index: 0 for index in range(1, die + 1)}

    generate = (lambda : randint(1, die)) if advantage == 0 \
            else (lambda : min(randint(1, die), randint(1, die))) if advantage < 0 \
            else (lambda : max(randint(1, die), randint(1, die)))

    for _ in range(attempts):
        rolls[generate()] += 1

    result = {}
    for key, value in rolls.items():
        result[key] = value / attempts

    return result

if __name__ == "__main__":
    res1= distribution(advantage=-1)
    res2 = distribution(advantage=0)
    res3 = distribution(advantage=1)

    for res in [res1, res2, res3]:
        print("{")
        for key, value in res.items():
            print(f"\t{key}\t: {(value * 100):.2f}%")
        print("}\n")
