s="22627191"
sumi=0
for i in s:
    sumi+=int(i)
print(sumi)
if sumi&1==0 and int(s[-1])&1==1:
    print("even but not even")
