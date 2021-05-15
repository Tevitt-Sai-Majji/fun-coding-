class Solution:
    def happy(self,n):
	    s=set()
	    while(True):
		    s.add(n)
		    if n==1:
			    return True
		    val=0
		    while(n>=1):
			    val+=(n%10)**2
			    n=n//10
		    n=val
		    if n in s:
			    return False
    def nextHappy(self,n):
	   if self.happy(n+1):
		    return n+1
	   return self.nextHappy(n+1)
