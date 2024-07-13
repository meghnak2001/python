#selection sort- swap the first element with the smallest element of the list and continue the process
#first 
'''
def selectionsort(a):
    n=len(a)
    for i in range(n//2-1):
        mn=i
        for j in range(i+1,n//2):
            
            if a[j]> a[mn]:
                mn=j
        a[i],a[mn]=a[mn],a[i]
    for i in range(n//2,n-1):
        mn=i
        for j in range(i+1,n):
            
            if a[j]<a[mn]:
                mn=j
        a[i],a[mn]=a[mn],a[i]

a=list(map(int,input().split()))
selectionsort(a)
print(a)

#bubble sort
def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        f=0
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

                f=1
        if f==0:
            break
        print(a)
a=list(map(int,input().split()))
bubblesort(a)

#insertion sort
def insertionsort(a):
    n=len(a)
    for i in range(1,n):
        t=a[i]
        j=i
        while j>0:
            if t<a[j-1]:
                a[j]=a[j-1]
            else:
                break
        a[j]=t
        print(a)
a=list(map(int,input().split()))
insertionsort(a)

#merge sort

def merge(a,l,m,r):
    n1=m-l+1
    n2=r - m
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        l[i]=a[l+i]
    for j in range(0,n2):
        R[j]=a[m+1+j]
    
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        a[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        a[k]=R[j]
        j+=1
        k+=1

def mergeSort(a,l,r):
    if l<r:
        m=l+(r+l)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)

#incomplete code 

#quick sort
def partition(a,low,high):
    pivot=a[high]
    i=low-1
    for j in range(low,high):





def quicksort(a, low, high):
    if low<high:
        pi=partition(a,low,high)
        quicksort(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)

a=list(map(int,input().split()))
n=len(a)
quicksort(a,0,n-1)
print("sorted array in ascending order:")
print(a)


'''

#heap sort
#radix sort
#bucket sort
#counting sort
#sort strings in dictionary order










