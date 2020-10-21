price=[8,4,6,2,3]
sp_price=[]
for i in range(len(price)):
    for j in range(i+1,len(price)):
        if price[i]>=price[j]:
            sp_price.append(price[i]-price[j])
            break
        else:
            sp_price.append(price[i])
print(sp_price)
    
