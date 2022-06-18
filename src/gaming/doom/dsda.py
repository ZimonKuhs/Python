import getopt
import os
import sys

def categorize(category):
    if not category:
        return ""

    converter = {
        "max": "",
        "speed": "",
        "uv": "",
        "uv-max": "",
        "uv-speed": "",

        "100s": "s",
        "nm100": "s",
        "nm": "n",
        "nms": "s",
        "nightmare": "n",

        "fast": "f",
        "pacifist": "p",
        "uv-p": "p",
        "uv-pacifist": "p",
        "respawn": "r",
        "tyson": "t",

        "nomo": "o",
        "none": "o",
        "no-monsters": "o",
        "no-mo": "o",
        "nomo100": "os",
        "only-secrets": "os",

        "collector": "col",
        "stroller": "str",
        "walk": "str",

        "misc": "",
        "other": "",
    }

    string = category.lower().replace(" ", "-")

    result = None
    for key, value in converter.items():
        if string == key or category == value:
            result = value
            break

    if result == None:
        # print("Warning: using 'other' category.")
        result = ""

    skill = 4
    if result == "n" or result == "s":
        skill = 5

    flags = {
        "f": ["fast"],
        "o": ["nomonsters"],
        "r": ["respawn"]
    }[result]

    return result, skill, flags


def d2Number(number):
    string = str(number)
    digits = len(string)

    if digits == 0 or digits > 2:
        raise ValueError(f"Invalid map number {number}")

    result = str(int(string))
    return result if len(result) == 2 else f"0{result}"


def mapNumber(level, iwad):
    string = str(level).lower()
    size = len(string)
    doom1 = wadCode(iwad) == ""

    if size == 0 or size > 5:
        raise ValueError(f"Illegal map-number string: {level}")

    if doom1:
        if size == 1:
            raise ValueError(f"Illegal map-number string: {level}")

        if size == 2:
            episode, map = int(string[0]), int(string[1])

            if episode < 1 or episode > 5 or map < 1 or map > 9:
                raise ValueError(f"Illegal map-number string: {level}")

            return f"e{episode}m{map}"

        if size == 3:
            if string[1] != "m":
                raise ValueError(f"Illegal map-number string: {level}")

            return f"e{str(int(string[0]))}m{str(int(string[2]))}"

        if size == 4:
            if string[0] != "e" or string[2] != "m":
                raise ValueError(f"Illegal map-number string: {level}")

            return f"e{str(int(string[1]))}m{str(int(string[3]))}"

    # DOOM 2 Numbering:

    if size <= 2:
        return f"{d2Number(string)}"

    if size == 3:
        if string[0] != "m":
            raise ValueError(f"Illegal map-number string: {level}")

        return f"{d2Number(string[1:])}"

    if size == 5:
        if string[0:3] != "map":
            raise ValueError(f"Illegal map-number string: {level}")
        return f"{d2Number(string[3:])}"

    raise ValueError(f"Illegal map-number string: {level}")


def wadCode(wadName):
    string = wadName.lower().replace(" ", "-")

    converter = {
        "d1": "",
        "doom1": "",
        "doomx": "",
        "doom1x": "",
        "ud": "",
        "ultimate-doom": "",

        "doom2": "lv",
        "doom-2": "lv",
        "tnt": "e",
        "plutonia": "pl",

        "alien-vendetta": "av",
        "hell-revealed": "hr",
        "memento-mori": "mm",
        "memento-mori-2": "m2",
        "requiem": "rq",
        "scythe": "sc"
    }

    result = None
    for key, value in converter.items():
        if string == key or wadName == value:
            result = value
            break

    if result == None:
        print(f"Warning: Couldn't find {wadName}")
        return None, None

    comp = 2
    if result == "e" or result == "pl":
        comp = 4
    elif result == "":
        comp = 3

    return result, comp


def usage(code):
    print(f"usage: {os.path.basename(__file__).replace('.py', '')} [-c CATEGORY] [-i IWAD] [-l LEVEL] [-p PWAD] [-w WAD CODE]")
    sys.exit(code)


def isDoom1(level):
    return len(level) == 4 or len(level.split()) == 2


def findIWAD(rootDir, code, subDirs = ["wad"]):
    name = "doom"
    if code == "lv":
        name = "doom2"
    elif code == "pl":
        name = "plutonia"
    elif code == "e":
        name = "tnt"

    return findWAD(rootDir, name, subDirs)



def findWAD(rootDir, code, subDirs = ["wad"]):
    name = f"{code.upper()}.wad"

    for dir in [""] + subDirs:
        search = os.path.join(rootDir, dir, name)

        if os.path.isfile(search):
            # print(f"Using {search}")
            return search

    raise FileNotFoundError(f"Couldn't find WAD {name}")


if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:i:l:p:")
    except getopt.GetoptError as error:
        usage()

    config = {
        "complevel": 2,
        "iwad": "",
        "record": "",
        "skill": 4,
        "warp": "",
    }
    additional = []

    doomDir = os.getenv("DOOM_ROOT")
    dsdaDir = os.getenv("DSDA_ROOT")

    if not os.path.exists(doomDir) or not os.path.exists(dsdaDir):
        raise ValueError("DOOM_ROOT and DSDA_ROOT must be set to existing directories!")

    category = "UV-Fast"
    level = "01"
    iwad = None
    pwad = ""
    code = ""

    for option, value in opts:
        if option == "-c":
            category = value
        elif option == "-i":
            iwad = value
        elif option == "-l":
            level = value
        elif option == "-p":
            pwad = value
        elif option == "-w":
            code = value
        else:
            raise ValueError(f"No such option: {option}")

    d1 = isDoom1(level)
    if not iwad:
        iwad = "doom1" if d1 else "doom2"

    if not code:
        if pwad:
            code, comp = wadCode(pwad)

            if not code:
                raise ValueError("If you specify a non-Compete-N PWAD, a PWAD *file code* must be set via -w!")
        else:
            code, comp = wadCode(iwad)

    number = mapNumber(level, iwad)
    mode, skill, flags = categorize(category)

    outFile = f"{code}{number}{mode}-MMSS"
    outDir = os.path.join(doomDir, "demo", iwad, category, "map" + level if len(level) == 2 else level)
    outPath = os.path.join(outDir, f"{outFile}.lmp")

    os.makedirs(outDir, exist_ok = True)

    for flag in flags:
        additional.append(flag)

    config["iwad"] = findIWAD(doomDir, code)
    config["complevel"] = comp
    config["record"] = outPath
    config["skill"] = str(skill)
    config["warp"] = f"{number[1]} {number[3]}" if d1 else number[-2:]

    if pwad:
        config["file"] = findPWAD(doomDir, code)

    command = f"{os.path.join(doomDir, 'dsda', 'dsda-doom.exe')}"
    for key, value in config.items():
        if key and value:
            command = f"{command} -{key} {value}"

    for flag in additional:
        command = f"{command} -{flag}"

    print(command)
