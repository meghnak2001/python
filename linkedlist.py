class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def insert_begin(self,x):
        nn=node(x)
        if self.head is None:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn


    def insert_end(self,x):
        nn=node(x)
        if self.head is None:
            self.head=nn
        else:
            i=self.head
            while i.next:
                i=i.next
            i.next=nn


    def insert_position(self,x,p):
        nn=node(x)
        if self.head is None:
            self.head=nn
        elif p==0:
            llist.insert_begin(x)
        else:
            j=0
            i=self.head
            while j<p-1:
                j+=1
                i=i.next
            nn.next=i.next
            i.next=nn


    def display(self):
        if self.head is None:
            print("Nothing to display")
        else:
            i=self.head
            while i is not None:
                print(i.data,end= "->")
                i=i.next


    def delete_begin(self):
        if self.head is None:
            print("nothing to delete")
        elif self.head.next is None:
            print(f'{self.head.data} deleted')
            self.head=None
        else:
            print(f'{self.head.data} deleted')
            self.head=self.head.next


    def delete_end(self):
        if self.head is None:
            print("nothing")
        elif self.head.next is None:
            print('f{self.head.data} is deleted')
            self.head=None
        else:
            i=self.head
            while i.next.next:
                i=i.next
            print(f'{i.next.data} is deleted')
            i.next=None

    def delete_position(self,p):
        if self.head is None:
            print("Nothing to delete")
        elif self.head.next is None:
            print('f{self.head.data} is deleted')
            self.head=None
        else:
            if p==0:
                llist.delete_begin()
            else:
                t=self.head
                i=0
                while i<p-1:
                    i+=1
                    


llist=SLL()
while True:
    print("\n 1.insert_begin\n 2.insert_end\n 3.insert_position\n 4.display\n 5.exit\n  6.delete_begin\n 7.delete_end \n 8.delete_position")

    ch=int(input())

    match ch:
        case 1:
            val = int(input())
            llist.insert_begin(val)
        case 2:
            val=int(input())
            llist.insert_end(val)
        case 4:
            llist.display()
        case 5:
            break 
        case 3:
            val,p=map(int,input().split())
            llist.insert_position(val,p)
        case 6:
            llist.delete_begin()

        case 7:
            llist.delete_end()
        case 8:
            p=int(input("Enter Position-"))
            llist.delete_position(p)