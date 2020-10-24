str1=input("enter 1st string:")
c=0
str2=input("enter 2nd string:")
j=min(len(str1),len(str2))
for i in range(j):
    if str1[i]!=str2[i]:
        c=c+1
if c==0:
    print("equal")
elif c<2:
    print("nearly equal")
else:
    print("different")
