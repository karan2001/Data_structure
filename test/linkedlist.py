class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head = None
        self.last = None
    def inse(self,data):
        if self.head == None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
            self.last.next = self.head
             
    def dis(self):
        curr=self.head
        while curr is not None:
            
            print(curr.data)
            print()
            if curr.next == self.head:
                break
            curr=curr.next
    def find(self,key):
        curr= self.head
        index = 0
        while curr:
            if curr.data==key:
                print(index)
                return
            else:
                curr=curr.next
                index+=1
    def dele(self,ind):
        c_id=0
        curr = self.head
        pre=None
        while curr is not None:
            if c_id == ind:
                if pre is not None:
                    pre.next = curr.next
                else:
                    self.head = curr.next
            pre=curr
            curr= curr.next
            c_id +=1
            pass
    def inany()
        
        
        
l=ll()
l.inse(5)
l.inse(6)
l.dis()
l.find(6)
l.dele(0)
print("\n\n")
l.dis()