class node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
    # def disn(self):
    #     return self.data

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

    def maxmin(self):
        if self.first!=None:
            s=0
            l=0
            temp=node(None)
            temp=self.first
            s=l=temp.data
            while temp != None:
                if(temp.data>l):
                    l=temp.data
                if(temp.data<s):
                    s=temp.data
                temp=temp.next
            print("smallest -> ",s)
            print("largest -> ",l)
        else:
            print("can't find max and min in empty list")

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
l.maxmin()