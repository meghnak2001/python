def heapify(a,i,n):
    l=2*i+1
    r=2*i+2
    mn=i
    if l<n and a[l]>a[mn]:
        mn=l
    if r<n and a[r]>a[mn]:
        mn=r
    if mn!=i:
        a[mn],a[i]=a[i],a[mn]
        heapify(a,mn,n)

a=list(map(int,input().split()))

n=len(a)

for i in range(n//2-1,-1,-1):
    heapify(a,i,n)

for i in range(n-1,0,-1):
    a[i],a[0]=a[0],a[i]
    heapify(a,0,i)
print(a)