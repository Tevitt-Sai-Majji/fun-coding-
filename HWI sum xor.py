import itertools
l=[]
count=0
def getpairs(N,M,X):
    if X>M:
        return
    global l,count
    print(l)
    if sum(l)>M or len(l)>5:
        return
    if len(l)==5:
        x=0
        s=0
        for i in l:
            s+=i
            x^=i
        if s==M and X==x:
            count+=1
            return
    for i in range(N+1):
        l.append(i)
        getpairs(N,M,X)
        l.pop()
    return
N=int(input())
M=int(input())
X=int(input())
getpairs(N,M,X)
print(count)
'''l=[]
m=M//2+1
for i in range(N+1):
    for j in range(N+1):
        l.append(j)
s=set(itertools.combinations(l,N))
count=0
for i in s:
    sumi=0
    xor=0
    for j in i:
        sumi+=j
        xor^=j
    if sumi==M and xor==X:
        count+=1
print(count)'''
