from functions import *


def main():
    LFuncs = [{"title": "EXIT", "func": None},
              {"title": "High Pass Filtering",      "func": highPassFiltering},
              {"title": "Canny Filtering",              "func": cannyFiltering},
              {"title": "Find a contour on a square",       "func": contour1},
              ]

    while True:
        print("\n" + "-"*15 + "Action Menu" + "-"*15)
        for i in range(len(LFuncs)):
            print(i, LFuncs[i]["title"])
        print()

        choice = -1
        while choice < 0 or choice >= len(LFuncs):
            msg = "Enter your choice (0-" + str(len(LFuncs) - 1) + "): "
            choice = int(input(msg))
        print()

        if choice != 0:
            LFuncs[choice]["func"]()
        else:
            break

if __name__ == '__main__':
    main()