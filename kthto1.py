
#change kth position to 1
def setbit(n,k):
    return n|(1<<k)

n,k=map(int,input().split())
print(setbit(n,k))