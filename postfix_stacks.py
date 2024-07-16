st=[]
s=input()
for i in s:
    if i.isdigit():
        st.append(i)
    else:
        v1=st.pop()
        v2=st.pop()
        res=eval(v2+i+v1)
        st.append(str(res))

print(st.pop())