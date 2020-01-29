import timeit
array = [23, 17, 5, 90, 12, 44, 38, 84, 77]


def bubbleSort(array):
    n = len(array)

    for i in range(n):

        for j in range(0, n-i-1):

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


start_time = timeit.timeit()
bubbleSort(array)
end_time = timeit.timeit()
print(end_time-start_time)

print()
print("Sorted array is:")
for i in range(len(array)):
    print(array[i]),
