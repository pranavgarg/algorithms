'''
infix to postfix converter
'''

class Stack:
  def __init__(self):
    self.items = []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop() if self.empty() is False else []
  def empty(self):
    return self.items == []
  def peek(self):
    return self.items[-1]

def infix_postfix(infix_exp):
  s = Stack()
  postfix_exp = ""
  operand = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  operator_dict = {"*":3, "/":3, "+":2,"-":2}
  for i in infix_exp:
    #check to see if there is an operator, push onto the stack
    if i.lower() in operand or i.isdigit():
    #check to see if its an operand
        postfix_exp = postfix_exp + i
    elif i == ")":
        while s.peek()!="(":
            postfix_exp = postfix_exp + s.pop()
        s.pop() #remove the parathesis
    elif i == "(":
        s.push(i)
    elif i in operator_dict:
        if s.empty() == False and operator_dict[s.peek()] >= operator_dict[i]:
            postfix_exp = postfix_exp + s.pop()
            s.push(i)
        else:
            s.push(i)
  while (s.empty()==False):
      postfix_exp = postfix_exp + s.pop()
  return postfix_exp

assert (infix_postfix("(a+b)*(c+d)"))=="ab+cd+*"
assert (infix_postfix("3+5*2"))=="352*+"
assert (infix_postfix("3*5*2")) == "35*2*"
assert infix_postfix("(A+B)*C-(D-E)*(F+G)") == 'AB+C*DE-FG+*-'
