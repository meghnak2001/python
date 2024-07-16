llist=[]
def push(val):
    if len(llist)==a:
        print("Overflow")
    else:
        llist.append(val)
    

a=int(input())
while True:
    print("1.Push 2.Pop 3.Display 4.Exit 5.isEmpty")

    ch=int(input())
    
    match ch:
        case 1:
            n=int(input())
            push(n)
        case 2:
            if len(llist)==0:
                print("Empty List")
            else:
                llist.pop()
        case 3:
            print(llist)
        case 4:
            break
        case 5:
            if len(llist)==0:
                print("isempty")
