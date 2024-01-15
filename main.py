import sys
import colorama
fileName = sys.argv[1] if len(sys.argv) == 2 else input("file>")

lines = []
oldLines = []
with open(fileName, "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].removesuffix("\n")
oldLines  =lines.copy()

while True:
    cmd = input(">")

    if cmd == "quit":
            exit()
    elif cmd == "save":
        with open(fileName, "w") as f:
            for i in range(len(lines)):
                lines[i] += "\n"
            f.writelines(lines)
            continue

    firstChar = ""
    number = ""
    for char in cmd:
        if char.isdigit():
            number+=char
            continue
        firstChar = char
        break

    if number != "":
        if firstChar == "d":
            lines.pop(int(number)-1)
        elif firstChar == "s":
            to = int(cmd[cmd.find("s")+1:])-1
            lines[int(number)-1], lines[to] = lines[to], lines[int(number)-1]
    else:
        if firstChar == "l":
            print()
            for i in range(len(lines)):
                line = lines[i]#.removesuffix("\n")
                print(f"{i+1}> {line}")
            print()
        elif firstChar == "e":
            line = int(cmd[1:])-1
            print(f"\n{lines[line]}")
            lines[line] = input()
        elif cmd == "com":
            print()
            for i in range(len(lines) if len(lines)>=len(oldLines) else len(oldLines)):
                if not i>=len(lines):
                    line = lines[i]
                    print(end=f"{i+1}> {line}")
                if not i>=len(oldLines):
                    oldLine = oldLines[i]
                    if len(lines)>=i:
                        if line != oldLine:
                            print(end="\033[33m")
                    print(f"\033[1000D\033[35C{i+1}> {oldLine}")
                    print(end="\033[39m")
                else: 
                    print()
            print()
        elif cmd == "n":
            lines.append("")
