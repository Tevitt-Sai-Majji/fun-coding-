def f(n,k):
    val=0
    c=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            val=i
            c+=1
            if c==k:
                return val
    for i in range(int(n**0.5),0,-1):
        if n%i==0:
            val=n//i
            if val!=i:
                c+=1
                if c==k:
                    return val
    return -1
p=f(142884,35)
print(p)
