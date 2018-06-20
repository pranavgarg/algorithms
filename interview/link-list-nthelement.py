'''
get the nth element from end in linklist
'''

class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.next = node
    def __repr__(self):
        print "{}".format(self.value)

class Linklist:
    def __init__(self):
        self.head = None

    def insert(self, value):
        temp = Node(value)
        if not self.head:
            self.head = temp
            return
        head = self.head
        while head and head.next != None:
            head = head.next
        head.next = temp

    def print_nth_from_end(self, n):
        head, it = self.head, self.head
        for i in range(n):
            if not it:
               return None
            it = it.next
        while it:
            head = head.next
            it = it.next
        return head.value

a = Linklist()
a.insert(10)
a.insert(20)
a.insert(30)
assert a.print_nth_from_end(1) == 30