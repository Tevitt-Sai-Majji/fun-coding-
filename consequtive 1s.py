n=int(input())
l=list(input().split())
c=0
c1=0
for i in l:
    if i=="1":
        c+=1
    if c1<c:
        c1=c
    elif i=="0":
        c=0
print(c1)
        
