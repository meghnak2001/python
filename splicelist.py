a=[10,20,30,40,50,60]

i=0
j=len(a)-1

while i<=j:
        a[i],a[j]=a[j],a[i]

        i+=1
        j-=1

print(a)