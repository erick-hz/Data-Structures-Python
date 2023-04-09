class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            print("Value already exists in the tree.")

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(self.root, "")
        else:
            print("Traversal type not supported.")
            return False

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left_child, traversal)
            traversal = self.preorder_traversal(start.right_child, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left_child, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right_child, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left_child, traversal)
            traversal = self.postorder_traversal(start.right_child, traversal)
            traversal += (str(start.value) + "-")
        return traversal


# Create a binary tree with root node as 1
tree = BinaryTree(1)

# Add nodes to the binary tree
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

# Print the binary tree in pre-order traversal
print("Pre-order traversal: " + tree.print_tree("preorder"))

# Print the binary tree in in-order traversal
print("In-order traversal: " + tree.print_tree("inorder"))

# Print the binary tree in post-order traversal
print("Post-order traversal: " + tree.print_tree("postorder"))
