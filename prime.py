def isprime(n):
    flag=0
    for i in range(2,n):  # for better time complexity (2, int(n**0.5)+1)4
        if n%i==0:
            flag+=1
    if flag==0:
        return True
    return False  


a=list(map(int,input().split()))
if all(isprime(i) for i in a):
    print("yes")
else:
    print("no")

# More methods 
#SIEVE OF ERATOSTHENES - START FROM 2 AND MARK ALL ITS MULTIPLE THEN 3 AND AGAIN TO THE SAME. ALL THE UNMARKED NUMBERS ARE PRIME NUMBERS. 

def SIEVEERA(n):
    s=[0]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if s[i]==0:
            for j in range(i*i,n+1,i):
                s[j]=1
    for i in range(2,n+1):
        if s[i]==0:
            print(i,end=" ")

n=int(input())
SIEVEERA(n)


#SIEVES UNDER METHOD 
def sievesunder(n):
    ns=int((n-1)/2)
    s=[0]*(ns+1)
    j=i
    while(i+j+2*i*j)<=ns:
            s[i+j+2*i*j]=1
            j+=1

    for i in range(1,ns+1):
        if s[i]==0:
            print(i*2+1,end=" ")

n=int(input())
sievesunder(n)