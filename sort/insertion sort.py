def insertionSort(nlist):
    for index in range(1, len(nlist)):

        currentvalue = nlist[index]
        position = index

        while position > 0 and nlist[position-1] > currentvalue:
            nlist[position] = nlist[position-1]
            position -= 1
            print(nlist)
        print(nlist)
        print()
        nlist[position] = currentvalue


nlist = [5, 2, 1, 6, 9]
print(nlist)
insertionSort(nlist)
print(nlist)
