arr=[0,3,4,5,3,2,1]
t=True
i=0
while i<len(arr)-1:
    if arr[i]<arr[i+1] and t==True:
        t=True
        i+=1
    elif arr[i]==arr[i+1]:
        break
    else:
        t=False
    if arr[i]>arr[i+1] and t==False:
        t=False
        i+=1
if i==len(arr)-1:
    print(True)
else:
    print(False)
