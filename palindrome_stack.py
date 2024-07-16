st=[]
def palindromecheck(s):
    for i in s:
        st.append(i)
    for i in s:
        if i!=st.pop():     
            return False
    return True

s=input()
print(palindromecheck(s))

#2nd method

st=[]
def palindromecheck(s):
    i=0
    while i<len(s)//2:
        st.append(s[i])
        i+=1
    if len(s)%2!=0:
        i+=1
    while i < len(s):
        if s[i]!=st.pop():
            return False
        i+=1
    return True
s=input()
print(palindromecheck(s))