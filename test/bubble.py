def bubble(array):
    n=len(array)

    for i in range(n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                print(array)
    
    print(array)

arr=[5,2,1,3,7,2,6]
bubble(arr) 