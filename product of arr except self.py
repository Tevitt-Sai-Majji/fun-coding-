def prod(arr,n)  
    res=[None]*n
    prod=1
    for i in range(n):#left cumsum
        prod=prod*arr[i]
        res[i]=prod
    prod=1#right update
    for i in range(n-1,0,-1):
        res[i]=res[i-1]*prod
        prod*=arr[i]
    res[0]=prod
    return res
 #product of all the elements in the arr except that individual element
