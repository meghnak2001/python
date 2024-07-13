def isanagram(s1,s2):
    d=dict()
    for i in s1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in s2:
        if i not in d:
            return False
        else:
            d[i]-=1
    for i in d:
        if d[i]!=0:
            return False
    return True

s1=input()
s2=input()
if isanagram(s1,s2):
    print("yes")
else:
    print("nooooooooo!!")
