a=[1,2,3,4,5,6]
for i in range(0,len(a),2):
    a[i],a[i+1]=a[i+1],a[i]


print(a)
    