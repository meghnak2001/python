#Sum of elements in a Matrix
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
s=0
for i in range(n):
        s=s+a[i][i]+a[i][n-1-i]

print(s)

#Sum of elemnts of boundary

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
s=0
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            s+=a[i][j]

print(s)


#Left Rotation
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        print(a[j][n-i-1],end=" ")
    print()


#Right Rotation
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        print(a[n-j-1][i],end=" ")
    print()
















