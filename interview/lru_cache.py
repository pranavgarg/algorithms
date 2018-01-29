'''
Design a LRU Cache - asked in amazon, 2 sigma, salesforce.
Used for finding items in constant time and adding and deleting items can be fast.
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dict:
            n = self.dict[key]
            #remove the item from the linklist
            self._delete(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.dict:
            self._delete(self.dict[key])
        n = Node(key, value)
        self._add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            n = self.head.next
            self._delete(n)
            del self.dict[n.key]

    def _delete(self, n):
        prev = n.prev
        next = n.next
        prev.next = next
        next.prev = prev
        return

    def _add(self, n):
        p = self.tail.prev
        p.next = n
        self.tail.prev = n
        n.prev = p
        n.next = self.tail

n = LRUCache(3)
n.set(10, "p")
n.set(20, "ks")
n.set(30, "pr")
n.set(40, "sa")
assert n.get(10) == -1




