#local and global

g=10
def display():
    global g
    g+=1
    return g

print(display())
print(g)

#factorial of a number
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input())
print(fact(n))


#sum of first n natural numbers
def sum(a):
    if a==0:
        return 0
    else:
        return a + sum(a-1) 
n=int(input())
print(sum(n))

        



#sum of the digits of a number

def digitsum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        r=n%10
        return r + digitsum(n//10)

n=int(input())
print(digitsum(n))

#reverse of a number
s=0
def reverse(n):
    global s
    if n==0:
        return 
    else:
        s=s*10+(n%10)
        reverse(n//10)

n=int(input())
reverse(n)
print(s)

#multiplication of two numbers2

def multiply(a,b):
    if a==0 or b==0:
        return 0
    else:
        return a+ multiply(a,b-1)
a,b=map(int,input().split())
print(multiply(a,b))


#floor value of logarithm value a base b

def logr(a,b):
    if a==1:
        return 0
    else:
        return 1+ logr(a//b,b)

a,b=map(int,input().split())
print(logr(a,b))

#GCD of 2 numbers
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b=map(int,input().split())
print(gcd(a,b))


#nth number in the fibonacci seriess

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input())
print(fib(n))
