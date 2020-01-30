class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data 
        self.left=left
        self.right=right̥̥̥̥̥   



class BinarySearchTree:
    def __init__(self):
        self.root=None 
    def insert(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            temp=self.root
            while True:
                if(temp.data>=val):
                    if(temp.left==None):
                        temp.left=Node(val)
                        break
                    else:
                        temp=temp.left
                elif(temp.data<val):
                    if(temp.right==None):
                        temp.right=Node(val)
                        break
                    else:
                        temp=temp.right
    def Preorder(self,node):
        if(node==None):
            return
        else:
            print(node.data,end=" ")
            self.Preorder(node.left)
            self.Preorder(node.right)
    def Inorder(self,node):
        if(node==None):
            return
        else:
            self.Inorder(node.left)
            print(node.data,end=" ")
            self.Inorder(node.right)
    def Postorder(self,node):
        if(node==None):
            return
        else:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.data,end=" ")
def search(root,key):
    if(root==None):
        return False
    if(root.data==key):
        return True
    elif(root.data<key):
        s=search(root.right,key)
        return
    else:
        s=search(root.left,key)
        return s

tree=BinarySearchTree()
tree.insert(6)
tree.insert(9)
tree.insert(5)
tree.insert(2)
tree.insert(15)
tree.insert(24)
tree.insert(14)
tree.insert(7)
tree.insert(8)
tree.insert(7)
tree.insert(2)
print()
print("Preorder Printing :")
tree.Preorder(tree.root)
print("\nInorder Printing :")
tree.Inorder(tree.root)
print("\nPostorder Printing :")
tree.Postorder(tree.root)
ser=int(input("enter the number to search :"))
print("\nSeraching for the element",ser ,end= str("......."))

if(search(tree.root,ser)):
    print("Found")
else:
    print("Not Found")