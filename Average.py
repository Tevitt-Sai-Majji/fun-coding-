def average(arr):
    arr.sort()
    return sum(arr[1:-1])/(len(arr)-2)
arr = list(map(int,input().split())) 
print(average(arr))
