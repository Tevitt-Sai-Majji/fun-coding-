a=int(input())
b=int(input())
def getfactors(a):
    sumi=1
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            sumi+=i
            if i!=a//i:
                sumi+=a//i
    return sumi
    print(sumi)
a1=getfactors(a)
a2=getfactors(b)
if a1==b and a2==a:
    print("Amicable Number")
else:
    print("Not Amicable Number")
