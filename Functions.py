
def fact(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f

a=int(input())
f=fact(a)
print(f)
b=int(input())
f=fact(b)
print(f)


def add(a:int,b:int) -> int:  #for specific datatype requirement
    c=a+b
    return c


#sum of prime in a list
def isprime(a):
    if a<=1:
        return False
    c=0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            c+=1
            break
    if c==0:
        return True
    return False

n=list(map(int,input().split()))
s=0
for i in n:
    if isprime(i):
        s=s+i

print(s)


def isprime(a):
    if a<=1:
        return False
    c=0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            c+=1
            break
    if c==0:
        return True
    return False

def primearray(a):
    for i in a:
       if isprime(i)==False:
           return False
       return True

n=list(map(int,input().split()))
if primearray(n):
    print("yes")
else:
    print("no")



#count matching characters in revrse string
s=input()
i=0
j=len(s)-1
c=0
for _  in range(len(s)//2):
    if s[i]==s[j]:
        c+=2
    i+=1
    j-=1

if len(s)%2==0:
    print(c)
else:
    print(c+1)

#check if there are any consecutive vowels

def isvowel(s):
    a=["a","e","i","o","u"]
    for i in range(len(s)):
        if s[i] in a and s[i+1] in a:
            return True
    return False
    
s=input()
if isvowel(s):
    print("no")
else:
    print("yes")



#Triangular sum
def triangularsum(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            a[j]=(a[j]+a[j+1])%10
    return a[0]

lst=list(map(int,input().split()))
print(triangularsum(lst))

















