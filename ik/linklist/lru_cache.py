# Complete the function below.
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = None
        self.hash_map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_full(self):
        return self.capacity == len(self.hash_map)

    def set(self, key, value):
        if key in self.hash_map:
            node_addr = self.hash_map[key]
            node = self.remove(node_addr)
            node.val = value
        else:
            if self.is_full():
                self.evict()
            node = Node(key, value)
        self.insert(key, node)

    def evict(self):
        free_node = self.tail.prev
        prev_node = free_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        del self.hash_map[free_node.key]
        # free_node would be automatically released

    def remove(self, key, node_addr):
        node_parent = node_addr.prev
        node_parent.next = node_addr.next
        del self.hash_map[key]
        return node_addr

    def insert(self, key, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.hash_map[key] = node

    def get(self, key):
        val = -1
        if key in self.hash_map:
            val = self.hash_map[key].val
            node_addr = self.hash_map[key]
            node = self.remove(key, node_addr)
            self.insert(key, node)
        return val


def implement_LRU_cache(capacity, query_type, key, value):
    lru = LRU(capacity)
    out = []
    for idx, type in enumerate(query_type):
        if type == 1:  # set
            lru.set(key[idx], value[idx])
        elif type == 0:
            out.append(lru.get(key[idx]))
    return out



query_type = [1, 1, 0, 1, 0, 1, 0]
key = [5, 10, 5, 15, 10, 5, 5]
value = [11, 22, 1, 33, 1, 55, 1]

print implement_LRU_cache(2, query_type, key, value)