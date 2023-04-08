# Implement a Queue class using a list. The class should have the following methods: enqueue(item), dequeue(), is_empty(), and size().

class Queue :
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.size())  # prints 3

print(q.dequeue())  # prints 1
print(q.dequeue())  # prints 2
print(q.dequeue())  # prints 3

print(q.is_empty())  # prints True







# Implement a circular queue using an array. The class should have the following methods: enqueue(item), dequeue(), is_empty(), is_full(), and size().

# Given a string of parentheses, write a function to determine if the string is balanced. For example, "(()())" is balanced, but ")()(" is not .

# Implement a function to reverse the order of elements in a queue. You should not use any additional data structures.

# Implement a function to find the minimum element in a queue. You should not modify the original queue.

# Implement a function to remove all occurrences of a given element from a queue.

# Given a queue of integers, write a function to find the sum of all the elements in the queue.

# Given two queues, write a function to merge them into a single queue.

# Given a queue of strings, write a function to reverse the order of the strings in the queue.

# Implement a function to find the maximum element in a queue. You should not modify the original queue.
