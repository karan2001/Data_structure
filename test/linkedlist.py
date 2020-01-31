class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list():
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
            self.last = self.head

    def disp(self):
        curr = self.head
        while curr is not  None:

            print(curr.data)
            print()
            curr = curr.next

            if curr == self.head:
                break

    def find(self, key):
        curr = self.head
        index = 0
        while curr:
            if curr.data == key:
                return index
            curr = curr.next
            index += 1
        return -1

    def delete(self, key):
        curr = self.head
        curr_id = 0
        pre = None
        while curr is not None:
            if curr_id == key:
                if pre is not None:
                    pre.next = curr.next
                else:
                    self.head = curr.next
            pre = curr
            curr = curr.next
            curr_id += 1


a = linked_list()

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.disp()

print()

# print(a.find(4))


print()
# a.delete(2)
# a.disp()
