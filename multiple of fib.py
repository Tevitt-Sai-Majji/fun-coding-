def fib(n,k):
    a=0
    b=1
    i=0
    j=1
    while 1:
        j+=1
        a,b=b,a+b
        if b%n==0:
            i+=1
            if i==k:
                print(j)
                print(b)
fib(2,3)
        
        
