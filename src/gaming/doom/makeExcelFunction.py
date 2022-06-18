import sys

switch = f"SWITCH({sys.argv[1]}2, "
string = f"{switch}"
firstComma=""
value = 0
for letter in ["E", "D", "C", "B", "A", "X"]:
    for sign in ["-", "", "+"]:
        string = f"{string}{firstComma}\"{letter}{sign}\", {value}"
        firstComma=", "
        value += 1

print(f"{string})")
