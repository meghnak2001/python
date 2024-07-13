#Linear Search complexity 1, n ,n 
def linearSearch(a,k):
    for i in range(len(a)):
        if a[i]==k:
            return i
    return -1
    
a=list(map(int,input().split()))
n=int(input())
print(linearSearch(a,n))

#Binary search

def binarySearch(a,k):
    start=0
    end=len(a)-1
    while start<=end:
        mid=(start+end)//2

        if a[mid]==k:
            return mid
        elif a[mid]>k:
            end=mid-1
        else:
            start=mid+1
    return -1
    
a=list(map(int,input().split()))
n=int(input())
print(binarySearch(a,n))

#binarySearch with recursion
def binarySearch(a,k,start,end):
    if start<=end:
        mid=(start+end)//2

        if a[mid]==k:
            return mid
        elif a[mid]>k:
            return binarySearch(a,k,start,mid-1)
        else:
            return binarySearch(a,k,mid+1,end)
            
    return -1
    
a=list(map(int,input().split()))
n=int(input())
start=0
end=len(a)-1
print(binarySearch(a,n,start,end))