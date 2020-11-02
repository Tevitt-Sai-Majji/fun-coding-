a=[4,5,6]
b=[10,9,1,8]
d=2
c=0
for i in a:
   for j in b:
      if abs(i-j)<=d:
         c+=1
         break
print(len(a)-c)
