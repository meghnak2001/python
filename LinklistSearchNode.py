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
    def search(self,k):
        i=self.head
        c=0
        while i:
            if i.data==k:
                return c
            c+=1
            i=i.next
        return -1



llist=SLL()
n=int(input())
for i in range(n):
    llist.insert_end(int(input()))
llist.display()
print()
k=int(input())
print(llist.search(k))