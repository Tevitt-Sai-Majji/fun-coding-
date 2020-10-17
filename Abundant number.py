n=int(input())
a=0
for i in range(1,int(n/2+1)):
    if n%i==0:
       a=a+i
if a>=n:
   print("Abundant Number")
