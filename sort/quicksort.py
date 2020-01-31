
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Driver code
arr=[1,2,3,4,5,0,9]
n = len(arr)-1
quickSort(arr, 0, n)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
