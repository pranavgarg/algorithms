'''
decimal to binary
'''
class Stack(object):
    def __init__(self):
        self.items = []
    def peek(self):
        return self.items[-1]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if len(self.items) > 0 else []
    def size(self):
        return len(self.items)
    def empty(self):
        return self.items == []

def decimal_binary(no):
    s = Stack()
    while no!= 0:
        s.push(no%2)
        no = no/2
    return_str = ""
    while s.empty()==False:
        return_str = return_str  + str(s.pop())
    return return_str

assert decimal_binary(4) == "100"
