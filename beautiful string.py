arr=[0]
n=int(input())
for i  in range(n):
    arr.append(int(input()))
arr1=[]
i=1
c=1
while (i)**2<=n:
    arr1.append(arr[i*i])
    i+=16
print(arr1)
s1=set()
for i in range(len(arr1)-1):
    for j in range(i+1,len(arr1)):
        if arr1[i]<=arr[j]:
            s1.add(i)
            s1.add(j)
print(s1)
if s1:
    print(len(s1))
else:
    print(1)




