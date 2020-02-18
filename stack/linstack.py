import os
os.system('cls')
# Node class
class node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
# Linked List class


class LinkedList:
    # Function to initialize the Linked List object

    def __init__(self):
        self.top = None
        self.last=None

    def push(self, val):
        if self.top == None:
            self.top = node(val)
            # self.last=self.top
        else:
            temp = self.top
            self.top = node(val)
            self.top.next=temp
            # self.last.next = node(val)
            # self.last=self.last.next

    def display(self):
        temp = self.top
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

    def pop(self): 
        if self.top is not  None:
            poppednode = self.top 
            self.top = self.top.next
            poppednode.next= None
            print("After pop")
            self.display()
            print()
            return poppednode.data 
        else:
            print("cannot pop an empty stack!!")
          
        
             





a_list = LinkedList()


while True:
    x= int(input("1.push\n2.pop\n3.quit\n"))
    
    if x==1:
        n = int(input("how many elements"))
        for i in range(n):
            data = (int(input("enter data: ")))
            a_list.push(data)
        a_list.display()
        print()

    if x==2:
        a_list.pop()
    if x==3:
        print("shutting down")
        os.system('cls')

        break
        
    else:
        print("Enter a Correct option!!")
        os.system('cls')
    
        
