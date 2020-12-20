n=int(input())
seive=[1 for i in range(n)]
def seivegenerate():
    i=2 
    while(i*i<=n):#2*2=4<=25 True
        if seive[i]==1:#seive[2]==1 True
            for j in range(i*i,n,i):#2*2=4
                seive[j]=0#
        i+=1 
    seive[0]=0
    seive[1]=0 
seivegenerate()
if seive[n]==1:
    print("prime")
else:
    print('not prime')
