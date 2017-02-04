ops = { “+”: (lambda x,y: x+y),  "- ": (lambda x,y: x-y),”*”:(lambda x,y: x*y),  "/ ":(lambda x,y: x/y)}

def postfix_cal(expr_list):
 l = len(expr_list)
 s = []
 for i in expr_list:
  num_val = i-‘0’
 if num_val => 0 and num_val <=9:
  s.append(num_val)
 else:
  temp = ops[i](s.pop(),s.pop())
  s.append(temp)
 return s

		
