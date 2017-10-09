from __future__ import print_function

class Node(object):
    """
    Node implementation
    """
    def __init__(self, payload=None, next_node=None):
        self.payload = payload
        self.next_node = next_node

    def get_payload(self):
        return self.payload

    def get_next(self):
        return self.next_node

    def has_next(self):
        return bool(self.next_node)

    def set_next(self, new_next):
        self.next_node = new_next
        return self.next_node

    def __str__(self):
        return self.payload

class LinkedList(object):
    """
    Singly-linked list implementation
    """
    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        return self.head

    def get_tail(self):
        current = self.head
        if not current or not current.has_next():
            return current

        while current.has_next():
            current = current.get_next()
        return current

    def insert(self, payload, new_node=None):
        if not new_node:
            new_node = Node(payload)
            
        new_node.set_next(self.head)
        self.head = new_node
        return self

    def append(self, payload, new_node=None):
        if not new_node:
            new_node = Node(payload)

        self.get_tail().set_next(new_node)
        return self

    def size(self):
        current = self.head
        node_count = 0
        while current:
            node_count += 1
            current = current.get_next()
        return node_count

    def reverse(self):
        new_head = self.get_head()
        new_list = LinkedList( head=Node( self.head.get_payload()) )
        current = self.head.get_next()
        while current:
            new_list.insert(current)
            current = current.get_next()
        return new_list

    def __repr__(self):
        current = self.head
        line = ""
        while current:
            line += "({}) -> ".format(current.__str__())
            current = current.get_next()
        line += "None"
        return line
            
if __name__ == '__main__':
    my_list = LinkedList( Node(payload='D') ).insert('C').insert('B').insert('A').append('E')
    print(my_list)
    new_list = my_list.reverse()
    print(new_list)





        
    

        
