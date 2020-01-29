class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data 
        self.left=left
        self.right=right
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
    
# Base Cases: root is null or key is present at root 
    if root==None:
        print("root not found")
        return
    
    if  root.data == key: 
        print("root is found")
        return 

    # Key is greater than root's key 
    if root.data < key: 
        return search(root.right,key) 
    
    else:
        search(root.left,key) 


tree=BinarySearchTree()
num=int(input("How many Node :"))
for i in range(num):
    val=int(input("enter the numbers :"))
    tree.insert(val)
print("Preorder Printing :")
tree.Preorder(tree.root)
print("\nInorder Printing :")
tree.Inorder(tree.root)
print("\nPostorder Printing :")
tree.Postorder(tree.root)
print()
search(tree.root,5)