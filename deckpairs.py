def deckpairs(arr):

    pairspairs = [arr.count(i) for i in set(arr)] 
    return len(set(pairs)) == 1 and pairs[0] >1 
arr = list(map(int,input().split())) 
print(deckpairs(arr))
