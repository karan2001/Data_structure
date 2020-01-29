class node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
    def disn(self):
        return self.data

class linlis:

    def __init__(self):
        self.first=None
        self.last=None

    def insert(self,n):
        if self.first is None:
            self.first=node(n)
            self.last=self.first
        else:
            self.last.next=node(n)
            self.last=self.last.next
    
    def delete(self):
        if self.last==None:
            print("cannot delete at empty linked list")
        elif self.last.next==self.last:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next

    def middle(self):
        if self.first!=None:
            l=[]
            temp=node(None)
            temp=self.first
            while temp != None:
                l.append(temp.data)
                temp=temp.next
            
            k=len(l)
            ind=int(k/2)
            if k%2!=0:
                print("middle element -> ",l[ind])
            else:
                print("middle elements are -> ",l[ind-1]," & ",l[ind])

        else:
            print("can't find middle element in empty list")

    def display(self):
        if self.first!=None:
            temp=node(None)
            temp=self.first
            print("--",end="")
            while temp != None:
                print(temp.disn(),end="--")
                temp=temp.next
            print("")
        else:
            print("can't print empty list")

l=linlis()
l.insert(1)
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(5)
l.insert(6)
l.middle()