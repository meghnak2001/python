def triangularsum(a,n):
    if n>1:
        for i in range(n-1):
            a[i]=(a[i]+a[i+1])%10
        triangularsum(a,n-1)
    return a[0]

a=list(map(int,input().split()))
n=len(a)
print(triangularsum(a,n))