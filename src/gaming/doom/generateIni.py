import getopt
import os
import sys
import win32com
import winshell

def assertFile(path):
    if not os.path.isfile(path):
        raise ValueError(f"{path} {'is a directory' if os.path.isdir(path) else 'does not exist'}.")
    return path



"""
    Gets the application options from sys.argv.

    Wrapper around getopt, essentially.
"""
def appOptions(shortOpts = {}, longOpts = [], usageLines = []):
    if not sys.argv or len(sys.argv) <= 1:
        return []

    try:
        opts, args = getopt.getopt(sys.argv[1:], shortOpts, longOpts)
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"

        for line in usageLines:
            print(line)

        sys.exit(1)

    result = {}

    for option, value in opts:
        toPut = value
        if toPut is None:
            toPut = True
        result[option.replace("-", "")] = toPut

    return result




def makeShortcut(name, configPath):
    wDir = r"D:\Gaming\DOOM"
    path = os.path.join(wDir, f"{name}.lnk")
    target = f"{wDir}\gzdoom.exe"
    icon = target
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Arguments = f"-config {configPath}"
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()


if __name__ == "__main__":
    args = sys.argv[1:]
    argc = len(args)

    if argc < 2:
        print(f"Usage: {os.path.basename(__file__).replace('.py', '')} baseFile \"Name String Parts\"")
        sys.exit(1)

    baseFile = assertFile(args[0])
    name = "_".join(args[1:])

    baseLines = None
    with open(baseFile) as contents:
        baseLines = contents.readlines()

    output = []
    for line in baseLines:
        output.append(line)

        if line == "[Global.Autoload]":
            output.append(f"Path=$PROGDIR/auto/{name}/**")

    iniFile = f"D:\Gaming\DOOM\config\{name}.ini"
    os.makedirs(f"/D/Gaming/DOOM/config/{name}", exist_ok = True)

    if os.path.exists(iniFile):
        if os.path.isdir(iniFile):
            raise ValueError(f"{iniFile} is a directory!")

        os.remove(iniFile)

    with open(iniFile, "w") as outFile:
        outFile.writelines(output)

    makeShortcut(name, iniFile)
