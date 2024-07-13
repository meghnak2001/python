s=input()
c0,c1=0,0
for i in s:
    if i=='0':
        c0+=1
    else:
        c1+=1
if c0==c1:
    print(len(s))
else:
    mn=min(c0,c1)
    print(2*mn+1)