def mergeSort(x, counter):
    if len(x) <= 1:
        return
    l = x[0:len(x)//2]
    r = x[len(x)//2:]
    mergeSort(l, counter)
    mergeSort(r, counter)
    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            counter.incrementCompares()
            x[k] = l[i]
            counter.incrementSwaps()
            i += 1
            k += 1
        else:
            x[k] = r[j]
            counter.incrementSwaps()
            j += 1
            k += 1
    while i < len(l):
        x[k] = l[i]
        counter.incrementSwaps()
        i += 1
        k += 1
    while j < len(r):
        x[k] = r[j]
        counter.incrementSwaps()
        j += 1
        k += 1