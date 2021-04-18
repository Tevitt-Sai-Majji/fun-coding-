def ispalandrome(n):
    n=str(n)
    for i in range(len(n)//2+1):
        if n[i]!=n[-i-1]:
            return False
    return True
n=int(input())
num1=n-1
num2=n+1
while True:
    s=num1+num2
    if ispalandrome(num1):
        if ispalandrome(num2):
            if ispalandrome(s):
                break
            else:
                n=n-1
                num1=n-1
                num2=n+1
        else:
            num2+=1
    else:
        num1-=1
print(s)
