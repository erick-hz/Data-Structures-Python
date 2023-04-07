# First, you'll want to import the built-in list class, which will serve as the underlying data structure for your stack. You can do this by including the following line at the top of your code:
from typing import List

# Next, you can create an empty stack by initializing an empty list:
stack: List[int] = []

# In this example, we've declared the stack to hold integers, but you can modify the code to support any data type you like.
# To add an element to the top of the stack, you can use the append() method:
stack.append(5)
stack.append(40)
stack.append(500)
stack.append(45)
stack.append(54)
stack.append(52)
stack.append(25)
stack.append(15)
stack.append(35)
stack.append(75)
stack.append(85)

# This will add the value 5 to the top of the stack.
# To remove an element from the top of the stack, you can use the pop() method:
top_element = stack.pop()

# This will remove the top element from the stack and store its value in the variable top_element.
# To check if the stack is empty, you can use the len() function:
if len(stack) == 0:
    print('Stack is empty')
else:
    print(stack)
