def isprime(i):
    c=0
    for j in range(2,int(i**0.5)+1):
        if i%2==0:
            return False
    return True
        
def ni(n):
    i=2
    c=0
    while(i**2<n):
        if isprime(i):
            c+=1
        i+=1
    return c
print(ni(10))
