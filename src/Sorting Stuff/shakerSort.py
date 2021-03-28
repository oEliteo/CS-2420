def shakerSort(x, counter):
    flag = True
    while flag:
        flag = False
        for i in range(0,len(x)-1):
            if x[i] > x[i+1]:
                counter.incrementCompares()
                x[i], x[i+1] = x[i+1], x[i]
                counter.incrementSwaps()
                flag = True
        for i in range(len(x)-2,-1,-1):
            if x[i] > x[i+1]:
                counter.incrementCompares()
                x[i], x[i+1] = x[i+1], x[i]
                counter.incrementSwaps()
                flag = True