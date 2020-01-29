def insertionSort(nlist):
    for index in range(1,len(nlist)):

        currentvalue = nlist[index]
        position = index 

        while position > 0 and nlist[position-1]>currentvalue:
            nlist[position]=nlist[position-1]
            position -=1
        nlist[position]=currentvalue
nlist=[14,46,43,27,57,41,45,21,70]
print(nlist)
import timeit
start=timeit.timeit()
insertionSort(nlist)
end=timeit.timeit()
print(end-start)
print(nlist)





