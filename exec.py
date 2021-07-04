import sys
def Write():
    i = 0
    while True:
        i += 1
        text = input("%d: "%i)
        if text == "q":
            print("-> QUIT <-")
            sys.exit(0)
def Print():
    print("-- Bug list --")
    print("-- <q:quit> --")
    Write()
Print()