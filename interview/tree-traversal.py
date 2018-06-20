escape = lambda y: y if not y else ' '
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "{} <- {} -> {}".format(self.left, self.val, self.right)
class Tree:
    def __init__(self, value):
        self.head = Node(value)

    def __repr__(self):
        print ("{} <- {} -> {}  ".format(self.head.left, self.head.val, self.head.right))

    def level_ordering(self):
        frontier = [self.head]
        level = {}
        parent = {self.head: None}
        i = 0
        while frontier != []:
            next = []
            for n in frontier:
                if n not in level:
                    level[n] = i
                    if n.left:
                        next.append(n.left)
                        parent[n.left] = n
                    if n.right:
                        next.append(n.right)
                        parent[n.right] = n
            i +=1
            frontier = next
        return level

t = Tree(10)
t.head.left = Node(5)
t.head.left.left = Node(1)
t.head.left.right = Node(7)
t.head.right = Node(20)
print t.level_ordering()

