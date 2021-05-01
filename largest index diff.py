a=[21, 13, 18, 10, 7, 3, 1,13,12,11,10,9,8,7,6]
st=[a[0]]
top=0
maxi=0
for i in range(1,len(a)):
    if st[top]>a[i]:
        st.append(a[i])
        top+=1
    else:
        maxi=max(maxi,len(st))
        st=[a[i]]
        top=0
maxi=max(maxi,len(st))
print(maxi-1)
