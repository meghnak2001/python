# Count characters in string
s=input()
c=[0]*123
for i in s:
    c[ord(i)]+=1
for i in range(97,123):
    if c[i]>0:              #for repeated charcacters only c[i]>1
        print(chr(i),c[i])


s=input()
c=[0]*123
for i in s:
    c[ord(i)]+=1
for i in s:
    if c[ord(i)]>1:
        print(i,c[ord(i)])
        break
        
#Special Character Count
s=input()
l,d,sp=0,0,0
for i in s:
    if ord(i) in range(65,91) or ord(i) in range(97,123):
        l+=1
    elif ord(i) in range(48,58):
        d+=1
    else:
        sp+=1
print(l,d,sp)

s=input()
s=s+" "
s1=""
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        s1=s1+s[i]
print(s)
