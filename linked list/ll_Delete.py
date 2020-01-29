class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
            
 
    def deleteNode2(self, item_id): 
          
        current_id = 0
        current_node = self.head
        previous_node = None
        
        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        
        return                     
    
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int (input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
a_llist.deleteNode2(4) 
print ("\nLinked List after Deletion at position 2: ")
a_llist.display()