'''
s = 'abcd'
p = "*c."
'''
def is_match(s, p, i=0, j=0):
    if i == len(s) and j == len(p):
        return True

    if i == len(s) and j!= len(p):
        for k in range(j, len(p)):
            if p[k] != "*":
                return False
        return True

    if s[i] == p[j]:
        return is_match(s, p, i+1, j+1)

    if p[j] == ".":
        return is_match(s, p, i+1, j+1)
    if p[j] == "*":
        return is_match(s, p, i+1, j) or is_match(s, p, i, j+1)
    return False

assert is_match("abcd","*c.") == True