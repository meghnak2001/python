#input list

a=list(map(int,input().split()))

#access element without comma

print(*a)

for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)


#sum of all elements

print(sum(a))

sum1=0
for i in a:
    sum1+=i

#ALL method- checks if all the elements in the list satisfy the conditions
#ANY METHOD- checks if any element of the list follows the condition

if all(i%2==0 for i in a ):
    print("all are even")