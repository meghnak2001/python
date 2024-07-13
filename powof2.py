def powerof(n):
    while n>1:
        d=n%2
        if d!=0:
            return False
        n=n//2
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    print(powerof(n))

"""
if n&(n-1)==0:
    return True
"""