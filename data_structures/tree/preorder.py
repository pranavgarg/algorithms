class Tree:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

class Traversal:
    def prefix(self, tree):
        if tree == None:
            return
        print tree
        self.prefix(tree.left)
        self.prefix(tree.right)
    def inorder(self, tree):
        if tree == None:
            return
        self.inorder(tree.left)
        print tree
        self.inorder(tree.right)
    def postorder(self, tree):
        if tree == None:
            return
        self.inorder(tree.left)
        self.inorder(tree.right)
        print tree

traverse = Traversal()
traverse.inorder(tree);