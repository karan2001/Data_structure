import array as arr

a= arr.array('i',[1,2,3])

b=arr.array('u',['a','b','c'])
b.remove('b')
a.remove(3)

print("the new array created is ")

for i in a:
    print(i)
print()
for i in b:
    print(i)

print(b.index('a'))