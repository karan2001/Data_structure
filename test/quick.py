def part(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<= pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    print(arr)
    return i+1



def quick(arr,low,high):
    if low<high:
        pi=part(arr,low,high)
        print()
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)

arr=[32,25,20,12,7,5,1]
n=len(arr)-1
quick(arr,0,n)

print(arr)
