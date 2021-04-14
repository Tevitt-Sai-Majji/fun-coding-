arr=[2,1,2]
m=0
m1=0
for i in range(len(arr)):
    if m < arr[i]:
        m1=m
        m=arr[i]
    elif m!=arr[i] and m1<arr[i]:
            m1=arr[i]
l=[m,m1]
print(l)
        
                  
