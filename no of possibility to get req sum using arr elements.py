def posibility(n,l,m,count,l1,start,p):
    if sum(l1)>m:
        l1.pop()
        return count,p
    if sum(l1)==m:
        if l1 not in p:
            l2=l1
            p.insert(count,l2)
            print(l1)
            count+=1
            l1.pop()
        return count,p
    else:        
        for i in range(start,n):
            l1.append(l[i])
            #print(l1)
            count,p=posibility(n,l,m,count,l1,i,p)
            if len(l1)>=1:
                l1.pop()
    return count,p

n=int(input())
l=list(map(int,input().split()))
m=int(input())
count=0
l1=[]
p=[]
print(posibility(n,l,m,count,l1,0,p))
