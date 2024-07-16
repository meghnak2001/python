'''
10 40 30 20 60 70 50
10 40
20 60
30 60
40 60
60 70
50 -1
70 -1
'''

a=list(map(int,input().split()))
b=[]
b.append(a[0])
for i in range(1,len(a)):
    if len(b)!=0:
        val=b.pop()
        while a[i]>val:
            print(val,a[i])
            if len(b)==0:
                break
            val=b.pop()
        if a[i]<val:
            b.append(val)
    b.append(a[i])

while len(b)!=0:
    print(b.pop(),-1)