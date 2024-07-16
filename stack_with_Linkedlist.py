
#linked List Implementation

class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class stack:
    def __init__(self):
        self.head=None

    def insert_begin(self,x):
        nn=node(x)
        if self.head is None:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn

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
llist=stack()
while True:
    print("\n 1.push \n 2.pop\n 3.Top element \n 4.exit\n 5.isempty \n 6.Display stack")
    ch=int(input())

    match ch:
        case 1:
            val = int(input())
            llist.insert_begin(val)
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
        