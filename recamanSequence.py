class Solution:
    lis=[]
    def recamn(self,i,n):
        if i==n:
            return
        if i==0:
            Solution.lis.append(0)
        elif Solution.lis[i-1]-i>0 and Solution.lis[i-1]-i not in Solution.lis:
            Solution.lis.append(Solution.lis[i-1]-i)
        else:
            Solution.lis.append(Solution.lis[i-1]+i)
        self.recamn(i+1,n)
    def recamanSequence(self, n):
        if len(Solution.lis)>=n:
            return Solution.lis[:n]
        self.recamn(len(Solution.lis),n)
        return Solution.lis
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends
