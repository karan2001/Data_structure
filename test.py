class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Clink:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        if self.head == None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
            self.tail.next=self.head
    def disp(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
            if current==self.head:
                break

a_list = Clink()
n = int(input("num"))
for i in range(n):
    data = int(input('enter data item'))
    a_list.append(data)

a_list.disp()
