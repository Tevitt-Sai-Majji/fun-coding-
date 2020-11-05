a="madam"
#1st method
if a==a[::-1]:
  print(True)
else:
  priint(False)
#2nd method
for i in range(int(len(a)/2)):
  if a[i]!=a[len(a)-i-1]:
    print(False)
    break
else:
  print(True)
