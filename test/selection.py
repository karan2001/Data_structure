def selection(arr):
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
            arr[i],arr[min]=arr[min],arr[i]
            print(arr)
    
    print("final:\n",arr)

arr=[5,2,1,6,9]

selection(arr)