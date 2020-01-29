import os
os.system('cls')
x=[]
ind1 = []
n=int(input('number of elements ? '))

for i in range(n):
    
    x.append(int(input("Enter the value: ")))
    i
    os.system('cls')

find=int(input("enter the nuber to be found: "))

os.system('cls')

print(f"searching for {find}.....")
found=None

for j in range(n):
    if x[j]==find:
        found=x[j]
        #print(f" the number {x[j]} is at the index",j)
        ind1.append(j)
        
    elif x[j]!=find:
        print("............")
if found == None :
    print("Search Unsuccessful")
if found==find:
    print("Search successfull")
if len(ind1)==1:
    print(f"The number {find} is found at index : " ,str(ind1))
if len(ind1)>1:
    print(f"the number {find} is found at indeces : ",str(ind1))    
