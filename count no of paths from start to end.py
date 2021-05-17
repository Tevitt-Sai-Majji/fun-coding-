class Solution:
    def numberOfPaths (self, n, m):
        dp=[[0]*n]*m
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
