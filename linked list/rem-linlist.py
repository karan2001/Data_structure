class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None 

class LinkedList: 

	def __init__(self): 
		self.head = None

	def insert(self, x): 

		new_node = Node(x) 

		if self.head is None: 
			self.head = new_node 
			return

		last = self.head 
		while last.next: 
			last = last.next

		last.next = new_node 

	def display(self): 
		temp = self.head 

		while temp: 
			print(temp.data, end = " ") 
			temp = temp.next

def removeNthFromEnd(head, k): 
	
	first = head 
	second = head 
	count = 1
	while count <= k: 
		second = second.next
		count += 1
	if second is None: 
		head.value = head.next.value 
		head.next = head.next.next
		return
	while second.next is not None: 
		first = first.next
		second = second.next
	first.next = first.next.next

# Driver code 

val = [1, 2, 3, 4, 5] 
k = 2
ll = LinkedList() 
for i in val: 
	ll.insert(i) 

print("Linked list before modification:"); 
ll.display() 

removeNthFromEnd(ll.head, k) 

print("\nLinked list after modification:"); 
ll.display() 

# This code is contributed by Dhinesh 
