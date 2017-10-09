'''
(()()()())

(((())))

(()((())()))
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

parans = {
    "}":"{",
    ")":"(",
    "]":"["
    }

def balance_paranthesis(paranthesis):
    s = Stack()
    allowed_parans = parans.values()
    for i in paranthesis:
        if i in allowed_parans:
            s.push(i)
        elif i in parans:
            x = s.pop()
            if  x != parans[i]:
                return False
    return True if s.empty() == True else False

balance_paranthesis("(())")


assert balance_paranthesis("(()()()())")==True
assert balance_paranthesis("[ { ( ) ]") == False
assert balance_paranthesis("( [ ) ]") == False
