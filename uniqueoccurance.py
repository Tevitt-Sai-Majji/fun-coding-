def single(arr,n):
    once=0
    twos=0
    for i in range(n):
        twos = twos | (once & arr[i])
        once = once ^ arr[i]
        common_bit_mask = ~(once & twos)
        once &= common_bit_mask
        twos &= common_bit_mask
        print(once ," ",twos," ",common_bit_mask)
        print(arr)
    return once
arr=[3,3,2,4,2,3,2]
print(single(arr,len(arr)))
