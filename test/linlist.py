class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None 
    def append(self,data):
        if self.head is None:
            self.head=node(data)
            self.last_node=self.head
        else:
            self.last_node.next=node(data)
            self.last_node=self.last_node.next
       
    def insert(self,data,position):
        temp=self.head
        if(position==0):
            self.head=node(data)
            self.head.next=temp
        else:
            temp=self.head
            previousnode=temp
            newnode=node(data)
            temp_pos=0
            while True:
                previousnode=temp
                temp=temp.next
                temp_pos+=1
                if(temp_pos==position):
                    newnode.next=temp
                    previousnode.next=newnode
                    break
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
a_llist=Linkedlist()
num=int(input("How many elements :"))
for i in range(num):
    data=int(input("enter  the numbers :"))
    a_llist.append(data)
position=int(input("\nenter the position to insert:"))
val=int(input("\nenter the number to insert:"))
a_llist.insert(val,position)
print("\nThe linked list is :\n",end=" ")
a_llist.display()