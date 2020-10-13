i=input()
s=0
while s>9 or s==0:
   for j in i:
        s=0
        s=s+int(j)
   i=str(s)
print(s)
