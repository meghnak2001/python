
def setbit(n,k):
    c=0
    while n>0:
        d=n%2 # or d=n&1
        if c==k:
            if d==1:
                return True
            else:
                return False
        n=n//2 # or n=n>>1
        c+=1

n,k=map(int,input().split())
print(setbit(n,k))


"""
def setbit(n,k):
    return n&(1<<k)
"""

"""

(n>>k)&1

"""