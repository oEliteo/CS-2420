def countingSort(x, counter):
    y = [0] * len(x)
    for i in x:
        y[i] += 1
    k = 0
    for i in range(len(y)):
        for j in range(y[i]):
            x[k] = i
            k += 1