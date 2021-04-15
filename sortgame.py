a=[2,1,3,5,4,6,7]
k=2
p,l=0,0
for i in range(len(a)):
    if a[0]<a[1]:
        p=a[1]
        a.append(a[0])
        a.remove(a[0])
    else:
        if p==a[0]:
            l+=1
        else:
            l=1
        p=a[0]
        a.remove(a[1])
        a.append(a[1])
    if l==k:
        break
print(a[0],l,i+1)
        
    
