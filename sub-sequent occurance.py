#Given an array of positive integers arr,
#find a pattern of length m that is repeated k or more times.
#A pattern is a subarray (consecutive sub-sequence)
#that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.
#Return true if there exists a pattern of length m
#that is repeated k or more times, otherwise return false.


arr=[1,2,1,2,1,3]
m=2
k=2
p,l=0,0
for i in range(len(arr)-m):
    ar=arr[i:i+m]
    for j in range(len(arr)-m):
        if ar==arr[j:j+m]:
            p+=1
        if l<p:
            l=p
if l>=p:
    print(True)
else:
    print(False)

    
