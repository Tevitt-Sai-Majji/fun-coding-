#navie pattren search algorithm
def search(txt,ptt):
    #txt is the text file and ptt is the string pattren
    n=len(txt)
    m=len(ptt)
    for i in range(n-m+1):
        #lehgth of txt file - pattren len
        j=0
        #to know letter count matched
        while(j<m):
            if txt[i+j]!=ptt[j]:
                break#not equal break
            else:
                j+=1#equal incrmnt
        if j==m:
            print("pattren found at : ",i)
txt="AAABAAABBBABAABA"
ptt="AABA"
search(txt,ptt)
