class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class SLL:
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
    def display(self):
        if self.head is None:
            print("Nothing to display")
        else:
            i=self.head
            while i is not None:
                print(i.data,end= "->")
                i=i.next
    def length(self):
        i=self.head
        c=0
        while i:
            c+=1
            i=i.next
        return c



llist=SLL()

while True:
    ch=int(input())
    if ch==1:
        llist.insert_end(int(input()))
    else:
        break
llist.display()
print()

print(llist.length())