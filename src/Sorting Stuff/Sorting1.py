#Trindon Woolsey
#CS-2420
#Professor Stander
#1:30pm-2:45pm

import sys
import random
import math
from bubbleSort import bubbleSort as Bubble
from shakerSort import shakerSort as Shaker
from selectionSort import selectionSort as Selection
from mergeSort import mergeSort as Merge
from quickSort import quickSort as Quick
from modQuickSort import modQuickSort as MQuick
from countingSort import countingSort as Counting
from Count import Count
sys.setrecursionlimit(50000)

def main():
    sorts = [Bubble, Shaker, Selection, Merge, Quick, MQuick]
    names = ["Bubble", "Shaker", "Selection", "Merge", "Quick", "MQuick"]
    for name in names:
        print("%15s" % (name), end='')
    print()
    for s in range(3, 13):
        size = 2 ** s
        print (s, end='')
        for sort in sorts:
            x = createMostlySortedList(size)
            c = Count()
            if(sort == Bubble or sort == Shaker or sort == Selection or sort == Merge):
                sort(x, c)
            else:
                sort(x, 0, len(x) - 1, c)
            print("%10.2f" % (math.log(c.getCompares(), 2)), end='')
        print()
        
def createRandomList(size):
    xlist = []
    for i in range(size):
        xlist.append(random.randint(0, size -1))
    return xlist
def createMostlySortedList(size):
    x = createRandomList(size)
    x[0], x[len(x)-1] = x[len(x)-1], x[0]
    return x
main()