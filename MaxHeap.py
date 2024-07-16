def heapify(a,i,n):
    l=2*i+1
    r=2*i+2
    mx=i
    if l<n and a[l]>a[mx]:
        mx=l
    if r<n and a[r]>a[mx]:
        mx=r
    if mx!=i:
        a[mx],a[i]=a[i],a[mx]
        heapify(a,mx,n)

a=list(map(int,input().split()))

n=len(a)

for i in range(n//2-1,-1,-1):
    heapify(a,i,n)
print(a)