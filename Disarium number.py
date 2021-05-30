n=input()
sumi=0
for i in range(len(n)):
    sumi+=int(n[i])**(i+1)
if sumi==int(n):
    print("Disarium number")
else:
    print("Not a Disarium number")
