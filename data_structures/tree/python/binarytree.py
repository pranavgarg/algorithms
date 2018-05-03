class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __repr__(self):
        return "%s" %(self.value)

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        self.preorder_print(self.root, traversal)
        return '-'.join([str(_) for _ in traversal])

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start == None:
            return False
        if start.value == find_val:
            return True

        found = self.preorder_search(start.left, find_val)
        if found == True:
            return found
        return self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start == None:
            return
        traversal.append(start.value)
        self.preorder_print(start.left, traversal)
        return self.preorder_print(start.right, traversal)

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
assert tree.search(5) == True
# Should be False
assert tree.search(6) == False

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()