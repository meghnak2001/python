a=[10,20,30,40,50]
n=len(a)
k=int(input())
k=k%n 
b=[]               # vey very important
for i in range(n-1):
    b.append([(i+k)%n])
print(b)


"""

Right Rotation 

a[k:]+a[:k]

"""