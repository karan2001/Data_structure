
class node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class circular_linked_list:
    def __init__(self, head=None):
        self.head = head

    def display(self):
        current = self.head
        while current is not None:
            print (current.key,end = ' ')
            current = current.next
            if current == self.head:
                break
    def pretty_print(self):

        cir_list_str = ''

        current_node = self.head

        while current_node:
            cir_list_str += '-({0:1d})-'.format(current_node.key)
            current_node = current_node.next
            if current_node == self.head:
                break

        return cir_list_str

    # Insert node at the end of the circular linked list
    def append(self, key):
        new_node = node(key)
        # If there are no elements in the circular linked list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
            # Traverse the circular linked list to find last node
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = self.head

   

    


if __name__ == "__main__":

    # Create circular linked list
    cir_list = circular_linked_list()

    data = [5, 8, 10, 12]

    for value in data:
        cir_list.append(value)

    cir_list.display()
    cir_list.pretty_print()
   