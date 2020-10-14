lis=[int(i) for i in input().split()]
key=int(input())
if key in lis:
  pass
else:
  lis.append(key)
print(lis.index(key))
