def insert(list):
    for i in range(1,len(list)):
        curr=list[i]
        position = i
        while position >0 and list[position-1]>curr:
            list[position]=list[position-1]
            position -=1
            print(list)
        print(list)

        list[position]=curr
    print("final\n",list)

arr=[5,2,1,6,9]

insert(arr)