from clint.textui import *

def Write():
    i = 0
    while True:
        i += 1
        text = input(colored.cyan("%d: "%i))
        if text == "q":
             sys.exit(0)
def Print():
    print(colored.cyan("-- Bug list --"))
    print(colored.cyan("-- ") + colored.red("<q:quit>") + colored.cyan(" --"))
    Write()
Print()
