dp=[0]*(10**6+1)
class Solution:
    def maxSum(self, n):
        mod=10**9+7
        n=n%mod
        r=n//2+n//3+n//4
        if r<=n:
            dp[n]=n
            return n
        else:
            return self.maxSum(n//2)+self.maxSum(n//3)+self.maxSum(n//4)
