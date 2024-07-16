que=[]
n=int(input())
def enqueue(x):
    if len(que)==n:
        print("Queue Overflow")
    else:
        que.append(x)

def dequeue():
    if len(que)==0:
        print("Queue underflow")
    else:
        print(f'{que.pop(0)} deleted')

def display():
    if len(que)==0:
        print("empty queue")
    else:
        print(que)

def front():
    if len(que)==0:
        print('Empty')
    else:
        print(que[0])

def isempty():
    if len(que)==0:
        print("YES EMPTY")
    else:
        print("NOT EMPTY")



while True:
    print("1. enqueue \n 2. Dequeue\n 3.display\n 4.front\n 5.isempty\n 6.break")

    ch=int(input())
    match ch:
        case 1:
            val =int(input())
            enqueue(val)
        case 2:
            dequeue()
        case 3:
            display()
        case 4:
            front()
        case 5:
            isempty()
        case 6:
            break
