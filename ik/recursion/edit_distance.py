'''
edit distance
'''
def edit_distance(s, p):
    return get_step_counts(s, p,0,0)


def get_step_counts(s, p, i, j):
    if i == len(s) and j == len(p):
        return 0
    if i==len(s):
        return len(p) - j
    if j == len(p):
        return len(s)-i
    if s[i] == p[j]:
        return get_step_counts(s,p,i+1,j+1)
    return min(get_step_counts(s,p,i,j+1), #Add
               get_step_counts(s, p, i+1, j), #remove
               get_step_counts(s, p, i+1, j + 1) #modify
               ) + 1 #current step

print edit_distance('ATTR', 'TTA')