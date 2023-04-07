# The Node class is defined with two attributes: data, which holds the data for the node, and next, which holds a reference to the next node in the list (or None if there is no next node)

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# The LinkedList class is defined with one attribute: head, which holds a reference to the first node in the list (or None if the list is empty).

class LinkedList:
    def __init__(self):
        self.head = None


# The append method is defined, which takes a data parameter and adds a new node with that data to the end of the list. If the list is empty, the new node becomes the head.

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


# The prepend method is defined, which takes a data parameter and adds a new node with that data to the beginning of the list. The new node becomes the new head, and its next attribute is set to the old head.

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


# The delete method is defined, which takes a data parameter and removes the first node in the list that contains that data. If the node to be deleted is the head, the head attribute is updated to reference the next node in the list.

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


# The print_list method is defined, which prints out the data in all of the nodes in the list, starting with the head.

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# An instance of the LinkedList class is created, and various methods are called to add nodes to the list, remove a node, and print the list.

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(3)
my_list.append(3)
my_list.prepend(0)
my_list.prepend(110)
my_list.delete(2)
my_list.delete(3)
my_list.print_list() 

