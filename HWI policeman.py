
n=int(input())
arr=[0]
k=int(input())
for i in range(n):
    arr.append(int(input()))
arr1=[0]*len(arr)
cost=0
for i in range(1,n-k-k+1):
    if arr[i+k]==1 and arr1[i]!=1:
        cost+=i+k
        for j in range(i,i+k+k+1):
            arr1[j]=1
for i in range(1,k+1):
    if arr[i]==1 and arr1[i]==0:
        cost+=i
        for j in range(1,i+k+1):
            arr1[j]=1
for i in range(n+1-k,n+1):
    if arr[i]==1 and arr1[i]==0:
        cost+=i
        for j in range(i-k,n+1):
            arr1[j]=1
for i in range(len(arr1)):
    if arr1[i]==0:
        arr1[i]=1
        cost+=i
print(cost)
        


        
