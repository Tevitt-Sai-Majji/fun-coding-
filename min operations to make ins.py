def fun(nums):
   c=0
   for i in range(1,len(nums)):
       if nums[i-1]>nums[i]:
          c+=nums[i-1]-nums[i]+1
          nums[i]=nums[i-1]+1
   return c
fun([1,1,1])
