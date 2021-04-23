#code
def prin(l):
    sum=0
    p=""
    while sum<=2*n:
        for i in range(n):
            if i<=sum:
                for j in range(n):
                    if i+j==sum and j<=sum:
                        p+=str(l[i][j])+" "
        sum+=1
    return p
                
    
for _ in range(int(input())):
    n= int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        l[i]=l[i*n:(i+1)*n]
    print(prin(l[:n]))
    
