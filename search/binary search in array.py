import os
os.system('cls')
x=[]
n=int(input('number of elements ? '))

for i in range(n):
    
    x.append(int(input("Enter the value: ")))
    os.system('cls')
# print(x)
x=sorted(x)
lenf=n
print(x)
middle=round(len(x)/2)
# print(middle)
# flag=0
find=int(input("Enter the number you want to find"))
def binary_search(mid,find):
    while True:
        if mid==0:
            return False
        if x[mid]==find:
            return mid
        elif x[mid]<find:
            mid=round(mid)+1
            return binary_search(mid,find)
        elif x[mid]>find:
            mid=round(mid/2)-1
            return binary_search(mid,find)
    


    
print(f"The number {find} is found at index ",binary_search(middle,find))
# if flag==0:
#     print("Search Unsuccessful!!!")