def isvalid(x):        
        st=[]
        top=-1
        for i in x:
            if i=="{" or i=="[" or i=="(":
                st.append(i)
                top+=1
            elif top!=-1:
                if i=="}" and st[top]=="{":
                    top-=1
                    st.pop()
                elif i=="]" and st[top]=="[":
                    top-=1
                    st.pop()
                elif i==")" and st[top]=="(":
                    top-=1
                    st.pop()
                else:
                    return False
            else:
                return False
            print(st)
        return len(st)==0
x="{}{(}))}"
print(isvalid(x))
