a=[1,2,3,1,1,0,0,0,1,2]
b=[0]
c=0
for i in range(1,len(a)):
    for j in range(i):
        if i<=j+a[j]:
            c=b[j]+1
            b.append(c)
            break
print(b)
print(b[len(a)-1])
