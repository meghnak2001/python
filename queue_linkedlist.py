
#linked List Implementation

class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class queue:
    def __init__(self):
        self.head=None

    def insert_end(self,x):
        nn=node(x)
        if self.head is None:
            self.head=nn
        else:
            i=self.head
            while i.next:
                i=i.next
            i.next=nn

    def Top_element(self):
        if self.head is None:
            print("is empty")
        else:
            print(self.head.data)


    def delete_begin(self):
        if self.head is None:
            print("under flow")
        elif self.head.next is None:
            print(f'{self.head.data} deleted')
            self.head=None
        else:
            print(f'{self.head.data} deleted')
            self.head=self.head.next

    def isempty(self):
        if self.head is None:
            print("is Empty")
        else:
            print("Not empty")
    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
llist=queue()
while True:
    print("\n 1.enqueue \n 2.dequeue\n 3.Front \n 4.exit\n 5.isempty \n 6.Display queue")
    ch=int(input())

    match ch:
        case 1:
            val = int(input())
            llist.insert_end(val)
        case 2:
            llist.delete_begin()
        case 3:
            llist.Top_element()
        case 4:
            break 
        case 5:
            llist.isempty()
        case 6:
            llist.display()
        