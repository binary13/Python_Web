import sys

argument = ""
if len(sys.argv) != 0:
    for arg in sys.argv:
        if sys.argv.index(arg) != 0:
            argument += arg + " "

print("Hello,", argument)