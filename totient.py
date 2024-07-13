def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def totient(n):
    c=0
    for i in range(2,n):
        if gcd(i,n)==1:
            c+=1
    return c

a=int(input())
print(totient(a))