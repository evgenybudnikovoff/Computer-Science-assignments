import sys
import math

task = 0
countArgv = len(sys.argv)

if countArgv <= 1:
    sys.exit("Error task not selected")
else:
    try:
        task = int(sys.argv[1])
    except ValueError:
        sys.exit("Input arguments not numbers") 

def main():
    match task:
        case 1:
            if countArgv <= 3:
                sys.exit("Error not enough arguments")
            else:
                try:
                    print("The largest number:", max(int(sys.argv[2]), int(sys.argv[3])), "\nThe smallest number:", min(int(sys.argv[2]), int(sys.argv[3])))
                except ValueError:
                    sys.exit("Input arguments not numbers")
        case 2:
            if countArgv <= 3:
                sys.exit("Error not enough arguments")
            else:
                try:
                    print("Square has a large area" if float(sys.argv[3]) ** 2 > math.pi * float(sys.argv[2]) ** 2 else "The circle has a large area")
                except ValueError:
                    sys.exit("Input arguments not numbers")
        case 3:
            if countArgv <= 4:
                sys.exit("Error not enough arguments")
            else:
                try:
                    print("Equation has real roots" if (int(sys.argv[3]) ** 2 - 4 * int(sys.argv[2]) * int(sys.argv[4])) >= 0 else "Equation has no real roots")
                except ValueError:
                    sys.exit("Input arguments not numbers")
        case 4:
            if countArgv <= 3:
                sys.exit("Error not enough arguments")
            else:
                try:
                    def task4(a, b):
                        if a > b:
                            return a
                        return b
                    print("Number", task4(float(sys.argv[2]), float(sys.argv[3])), "is the largest")
                except ValueError:
                    sys.exit("Input arguments not numbers")
        case 5:
            if countArgv <= 4:
                sys.exit("Error not enough arguments")
            else:
                try:
                    # print("Number", min(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])), "is the smallest")

                    a, b, c = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
                    smallest = a
                    if b < smallest:
                        smallest = b
                    if c < smallest:
                        smallest = c
                    print("Number", smallest, "is the smallest")
                except ValueError:
                    sys.exit("Input arguments not numbers")
        case 6:
            if countArgv <= 5:
                sys.exit("Error not enough arguments")
            else:
                try:
                    num = 0
                    it = 0
                    while(it < 4):
                        if float(sys.argv[it + 2]) < 0:
                            num += 1
                        it += 1
                    print("There are", num, "negative numbers")
                except ValueError:
                    sys.exit("Input arguments not numbers")
        case 7:
            if countArgv <= 4:
                sys.exit("Error not enough arguments")
            else:
                try:
                    print("Even numbers")
                    it = 0
                    while(True):
                        if (int(sys.argv[it + 2]) % 2) == 0:
                            print(int(sys.argv[it + 2]))
                        it += 1
                        if it >= 3:
                            break
                except ValueError:
                    sys.exit("Input arguments not numbers")
        case 8:
            if countArgv <= 2:
                sys.exit("Error not enough arguments")
            else:
                try:
                    FPOINT = 1
                    SPOINT = 6
                    x = float(sys.argv[2])
                    y = 0 if countArgv == 3 else sys.argv[3]

                    def task8(p):
                        if p < FPOINT:
                            return "I"
                        if p > SPOINT:
                            return "III"
                        return "II"
                    print("Point (", x, ", ", y, ") falls into area ", task8(x), sep = "")
                except ValueError:
                    sys.exit("Input arguments not numbers")

if __name__ == "__main__":
    main()