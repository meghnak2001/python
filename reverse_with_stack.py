llist=[]
n=int(input())
for i in str(n):
    llist.append(i)

sum=0
for i in range(len(llist)):
    sum=sum*10+int(llist.pop())

print(sum)



