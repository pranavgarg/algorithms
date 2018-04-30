'''
stack such that getMinimum() is an O(1) operation
'''
class MyStack:
    def __init__(self):
        self.stack = []
        self.minElement = None

    def getMin(self):
        if not self.stack:
            return None
        return self.minElement

    def peek(self):
        if not self.stack:
            return None
        t = self.stack[-1]
        if t < self.minElement:
            return self.minElement
        else:
            return t

    def push(self, element):
        if not self.stack:
            self.minElement = element
            return self.stack.append(self.minElement)

        if element < self.minElement:
            self.stack.append(2*element - self.minElement)
            self.minElement = element
        else:
            self.stack.append(element)

    def pop(self):
        if not self.stack:
            return None
        t = self.stack.pop()
        if t < self.minElement:
            actual = self.minElement
            self.minElement = self.minElement*2 - t
            return actual
        return t

a = MyStack()
a.push(3)
a.push(5)
assert a.getMin() == 3
a.push(2)
a.push(1)
assert a.getMin() == 1
print a.pop()
assert a.getMin() == 2