'''
s="abcd"

'''
def reverse_string(s):
  return reverse(list(s),0, len(s)-1)

def reverse(s, i, j):
    if i > j:
        return ''.join(s)
    s[j], s[i] = s[i], s[j]
    return reverse(s, i+1, j-1)

print reverse_string("abcd")