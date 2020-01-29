class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
            # self.last_node.next=self.head

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
            # if current.next==self.head:
            #     break
        print(self.head)

    def find(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
        return -1

    def delete(self, index):
        c_id = 0
        c_node = self.head
        pre_node = None
        while c_node is not None:
            if c_id == index:
                if pre_node is not None:
                    pre_node.next = c_node.next
                else:
                    self.head = c_node.next
            pre_node = c_node
            c_node = c_node.next
            c_id += 1


a_list = linkedlist()
n = int(input("num"))
for i in range(n):
    data = int(input('enter data item'))
    a_list.append(data)

a_list.display()
f = int(input("find?"))
if a_list.find(f) == -1:
    print("the value is not found in the linked list")
else:
    print(a_list.find(f))

a_list.delete(0)

a_list.display()

