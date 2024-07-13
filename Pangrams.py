def ispangram(s):
    c=[0]*123
    for i in s:
        c[ord(i)]+=1
    for i in range(97,123):
        if c[i]==0:
            return False
    return True
s=input()
if ispangram(s):
    print("yes")
else:
    print("no")
