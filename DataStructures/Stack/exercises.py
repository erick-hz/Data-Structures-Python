# 1.Implement a function reverse_string(string: str) -> str that takes a string as input and returns the string reversed using a stack. For example, reverse_string("hello") should return "olleh".

def reverse_string(string: str) -> str:
    stack = []
    reversed_string = ''
    # push each character of the string onto the stack
    for char in string:
        stack.append(char)
    # pop each character from the stack to construct the reversed string
    while len(stack) > 0:
        reversed_string += stack.pop()
    print(reversed_string)

reverse_string('hello')

# 2.Implement a function is_balanced(expression: str) -> bool that takes a string containing parentheses, brackets, and curly braces as input and returns True if the brackets are balanced and False otherwise. For example, is_balanced("([]){{}}") should return True, while is_balanced("([]}{)") should return False.


def is_balanced(expression: str) -> bool:
    stack = []  # Initialize an empty stack to keep track of opening brackets

    for char in expression:  # Loop through each character in the input string
        if char in '([{':  # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in ')]}':  # If the character is a closing bracket, check if it matches the top of the stack
            if not stack:  # If the stack is empty, there is no matching opening bracket
                return False
            # Pop the top of the stack and compare it to the closing bracket
            opening_bracket = stack.pop()
            if (opening_bracket == '(' and char != ')') or \
               (opening_bracket == '[' and char != ']') or \
               (opening_bracket == '{' and char != '}'):  # If the opening/closing brackets don't match, the expression is unbalanced
                return False

    # If the stack is not empty, there are unmatched opening brackets and the expression is unbalanced. Otherwise, the expression is balanced.
    return not stack


# Example usage and output:
print(is_balanced("([]){{}}"))  # True
print(is_balanced("([]}{)"))  # False

# 3.Implement a function evaluate_postfix(expression: str) -> int that takes a postfix arithmetic expression as input and returns the result. For example, evaluate_postfix("34+2*") should return 14 (which is equivalent to(3+4)*2).

# 4.Implement a function reverse_stack(stack: List[int]) -> List[int] that takes a stack represented as a list of integers as input and returns a new stack with the elements reversed(using only the basic stack operations). For example, reverse_stack([1, 2, 3, 4, 5]) should return [5, 4, 3, 2, 1].
