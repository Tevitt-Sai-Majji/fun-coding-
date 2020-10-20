# [i,j,.....n times] j should be printed i times
inp=[1,2,3,4]
op=[]
for i in range(0,len(inp),2):
    op+=[inp[i+1]]*inp[i]
print(op)
