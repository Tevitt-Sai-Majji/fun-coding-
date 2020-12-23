x=100
sieve=[1 for i in range(x+1)]
sieve[0]=0
sieve[1]=0
summ=[]
def sumsieve(end):
    i=0
    while(i*i<=end):
        if sieve[i]==1:
            for j in range(i*i,end+1,i):
                sieve[j]=0
        i+=1
    summ.append(0)
    for i in range(end):
        summ.append(sieve[i+1]*(i+1)+summ[-1])
sumsieve(x)
for _ in range(int(input())):
    start,end=map(int,input().split())
    print(summ[end]-summ[start-1])
