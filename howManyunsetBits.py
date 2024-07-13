def unset(n):
    c=0
    while n>0:
        d=n%2 # or d=n&1
        if d==0:
            c+=1
        n=n//2 # or n=n>>1
    return c

t=int(input())
for _ in range(t):
    n=int(input())
    print(unset(n))