import math;

def printpowerset(set, setsize):

    powersetsize = (int) (math.pow(2, setsize))

    outer = 0

    inner = 0

    for outer in range (0, powersetsize):

        for inner in range(0, setsize):

            if((outer & (1 << inner)) > 0):

                print(set[inner], end = " ")

        print("") 

size = int(input("Input array size: "))
set = []

for i in range(0, size):

    n = int(input("Input array element: "))
    set.append(n)

printpowerset(set, len(set))    