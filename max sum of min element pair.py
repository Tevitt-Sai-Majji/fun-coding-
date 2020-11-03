nums=list(map(int,input().split()))
#takes an array as input
nums.sort()
#to get the min elements in a pair we are sorting the array and taking the alternate values in the arr
#by adding all those alternate elemments we get the max sum of min element in a random pair
print(sum(nums[::2]))
