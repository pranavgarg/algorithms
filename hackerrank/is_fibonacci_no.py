'''
No entered is fibonacci or not.
Using binet's formula
https://www.hackerrank.com/challenges/is-fibo/topics/binets-formula
'''
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def binet_formula(num):
    # a fibonacci number should be having
    #  5*(num^2) + 4 or 5*(num^2) - 4  must be a perfect square
    x1 = 5*(num**2)
    if is_square(x1 + 4):
        return True
    elif is_square(x1 - 4):
        return True
    else:
        return False

def is_fibonacci(num):
    return binet_formula(num)

assert is_fibonacci(5) == True
assert is_fibonacci(4) == False
