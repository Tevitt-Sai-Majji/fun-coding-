a=[2,3,1,3,2,4,6,7,9,2,19] 
b=[2,1,4,3,9,6] 
l=[] 
for i in b: 
    l.extend([i]*a.count(i)) 
c=set(a)-set(b) 
c=list(c) 
c.sort() 
l.extend(c) 
print(l)
