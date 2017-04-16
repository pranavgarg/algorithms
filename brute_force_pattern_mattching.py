'''
Brute Force Pattern Matching
'''

def brute_force(input, text):
  i = 0
  c = 0
  while (c < len(text) and i < len(input)):
    if input[c] == input[i]:
      i = i + 1
    else:
      i = 0
    c = c + 1
  return (i == len(input))

assert False == brute_force('hello','hi')
assert False == brute_force('hello','')
assert True == brute_force('','hi')
assert True  == brute_force('hello','hello')
