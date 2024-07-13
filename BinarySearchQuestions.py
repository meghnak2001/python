#Peak elemnt in a array with binary search

def binarySearch(a):
    start=0
    end=len(a)-1
    while start<end:
        mid=(start+end)//2

        if a[mid]<a[mid+1]:
            start=mid+1
        
        else:
            end=mid
    return start
    
a=list(map(int,input().split()))
print(binarySearch(a))