n=5000
sum=0
import timeit
start=timeit.timeit()
for i in range(1,n*n):
    for j in range(0,i):
        sum=sum+1
end=timeit.timeit()
time=end-start
print(time)