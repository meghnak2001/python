def count(a,b):
    c=0
    while a>0 and b>0:
        d=a%2
        e=b%2 # or d=n&1
        if d^e==1:
            c+=1
        a=a//2
        b=b//2 # or n=n>>1
    return c

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(count(a,b))