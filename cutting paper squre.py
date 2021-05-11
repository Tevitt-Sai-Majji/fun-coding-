n,m=map(int,input().split())
c=0
if n>m:
    c=n-1+n*(m-1)
else:
    c=m-1+m*(n-1)
print(c)
