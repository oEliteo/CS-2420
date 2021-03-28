def selectionSort(x, counter):
    for i in range(len(x)):
        smallest = i
        for j in range(i, len(x)):
            if x[j] < x[smallest]:
                counter.incrementCompares()
                smallest = j             
        x[i], x[smallest] = x[smallest], x[i]
        counter.incrementSwaps()