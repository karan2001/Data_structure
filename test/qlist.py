class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class q:
    def __init__(self):
        self.rear=None
        self.front=None
    def en(self,val):
        temp =node(val)
        if self.rear is None:
            self.front=self.rear=temp
            
        self.rear.next=temp
        self.rear=temp
        return
    def de(self):
        if self.front is None:
            print("nothing to dequeue")
        temp=self.front
        self.front =temp.next

        if self.front is None:
            self.rear= None
        return str(temp.data)

    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end=' ')
            current = current.next  

q = q() 
q.en(10) 
q.en(20) 
q.de() 
q.de() 
q.en(30) 
q.en(40) 
q.en(50)  
q.display()