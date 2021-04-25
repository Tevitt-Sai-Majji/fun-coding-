N=100
primes=[1]*N
strong_prime=[0]*N
def strongs(l,m,h):
  if 2*m>l+h:
    return True
  return False
def creat_seive():
  primes[0]=primes[1]=0
  first=2
  second=3
  for i in range(2,N):#i=3
    if primes[i]==1:#T
      curr=i
      if i>=5 and strongs(first,second,curr):#2,3,5
        strong_prime[i]=1
     for j in range(i*i,N,i):#j 9,N,3
        primes[j]=0
     first=second
     second=curr
creat_seive()
print(primes)
