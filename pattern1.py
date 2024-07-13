'''
5 
4 5
3 4 5
2 3 4 5
1 2 3 4 5
'''
for i in range(5,0,-1):
    for j in range(i,6,+1):
        print( j, end=" ")
    print()

'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print( j, end=" ")
    print()  


'''
A
A B
A B C
A B C D

'''

for i in range(1,5,+1):
    for j in range(1,i+1,+1):
        print( chr(64+j), end=" ")
    print()

'''
E D C B A
D C B A
C B A
B A
A
'''
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print( chr(64+j), end=" ")
    print()


