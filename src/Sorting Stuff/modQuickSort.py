def modQuickSort(x, low, high, counter):
    if high - low <= 0:
        return
    mid = ((low + high) // 2)
    x[low], x[mid] = x[mid], x[low]
    counter.incrementSwaps()

    pivot = low
    lmbt = low + 1
    for i in range(low+1, high+1):
        if x[i] < x[low]:
            counter.incrementCompares()
            x[i], x[lmbt] = x[lmbt], x[i]
            counter.incrementSwaps()
            lmbt += 1
        pivot = lmbt - 1
    x[low], x[pivot] = x[pivot], x[low]
    counter.incrementSwaps()
    modQuickSort(x,low, pivot-1, counter)
    modQuickSort(x,pivot+1, high, counter)