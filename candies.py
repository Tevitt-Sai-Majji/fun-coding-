#distrubation of candies with minimal no of candies
'''c=[2 ,4 ,2 ,6 ,1 ,7 ,8 ,9 ,2 ,1]
s1=[1 , 2, 1, 2, 1, 2, 3, 4, 1, 1]'''
c=[2 ,4 ,3 ,5 ,2 ,6 ,4 ,5]
s=[0]*len(c)
s[0]=1
for i in range(1,len(c)):
    if c[i-1]<c[i]:
        s[i]=s[i-1]+1
    else:
        s[i]=1
count=0
for i in range(len(c)-2,-1,-1):
    if c[i+1]<c[i] and not count:
        count+=1
    elif c[i+1]<c[i] and count:
        s[i]+=count
        count+=1
    else:
        count=0
    
#print(sum(s1))
print(sum(s))
