# Write a Python function to create a binary search tree(BST) from a given list of values. The function should return the root node of the tree.\

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def createBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = Node(nums[mid])

    root.left = createBST(nums[:mid])
    root.right = createBST(nums[mid+1:])

    return root


def printBST(node, level=0):
    if node is None:
        return

    printBST(node.right, level+1)
    print('   '*level + str(node.val))
    printBST(node.left, level+1)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = createBST(nums)
    printBST(root)


    

# Write a Python function to traverse a binary tree in pre-order, in -order, and post-order. The function should take the root node of the tree as input and print the node values in the specified order.

# Write a Python function to find the maximum depth of a binary tree. The function should take the root node of the tree as input and return the maximum depth.

# Write a Python function to find the lowest common ancestor(LCA) of two nodes in a binary search tree. The function should take the root node of the tree and the two nodes as input and return the LCA.

# Write a Python function to serialize and deserialize a binary tree. The function should take the root node of the tree as input and return a string representation of the tree. The deserialization function should take the string representation as input and return the root node of the tree.
