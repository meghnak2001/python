class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None


    def insert_begin(self,val):
        nn=node(val)
        if self.head is None:
            self.head=nn
            self.tail=nn
            
        else:
            nn.right=self.head
            self.head.left=nn
            self.head=nn
    

    def insert_end(self,val):
        nn=node(val)
        if self.head is None:
            self.head=nn
            self.tail=nn
        else:
            self.tail.right=nn
            nn.left=self.tail
            self.tail=nn
    def insert_position(self,val,p):
        nn=node(val)
        if self.head is None:
            self.head=nn
            self.tail=nn
        elif p==0:
            llist.insert_begin(val)
        
        else:
            t=self.head
            i=0
            while i<p-1:
                i+=1
                t=t.right
            if t.right is None:
                llist.insert_end(val)
            nn.right=t.right
            t.right.left=nn
            nn.left=t
            t.right=nn


    def display(self):
        if self.head is None:
            print("Nothing to display")
        else:
            i=self.head
            while i:
                print(i.data, end="->")
                i=i.right


    def display_reverse(self):
        if self.head is None:
            print("Nothing to display")
        else:
            i=self.tail
            while i:
                print(i.data,end="->")
                i=i.left


    def delete_begin(self):
        if self.head is None:
            print("Nothing to delete")
        elif self.head.right is None:
            print(f'{self.head.data} deleted')
            self.head,self.tail=None,None
        else:
            print(f'{self.head.data} deleted')
            self.head=self.head.right
            self.head.left=None

    def delete_end(self):
        if self.head is None:
            print("Nothing to delete")
        elif self.head.right is None:
             print(f'{self.head.data} deleted')
             self.head,self.tail=None,None
        else:
            print(f'{self.tail.data} deleted')
            self.tail=self.tail.left
            self.tail.right=None


    def delete_position(self,p):
        if self.head is None:
            print("Nothing to delete")
        elif self.head.right is None:
             print(f'{self.head.data} deleted')
             self.head,self.tail=None,None
        elif p==0:
            llist.delete_begin()
        else:
            t=self.head
            i=0
            while i<p-1:
                i+=1
                t=t.right
            if t.right.right is None:
                llist.delete_end()
            else:
                print(f'{t.right.data} deleted')
                t.right=t.right.right
                t.right.left=t


llist=DLL()
while True:

    print("1.insert_begin 2.insert_end 3.insert_position 4.display 5.exit  6.display_reverse 7.delete_begin 8.delete_end 9.delete_position")


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
            llist.display_reverse()

        case 7:
            llist.delete_begin()
        case 8:
            llist.delete_end()

        case 9:
            p=int(input("Enter Position-"))
            llist.delete_position(p)
