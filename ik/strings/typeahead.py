'''
Brute Force
N Words
M length
Given a dictionary of words return the words which match a prefix
'''

def get_words_matching_prefix(d, p):
    matches = []
    for w in d:
        if len(w) < len(p):
            continue
        if is_match(w, p):
            matches.append(w)
    return matches

def is_match(w, p, i=0, j=0):
    if j == len(p):
        return True
    if w[i] != p[j]:
        return False
    else:
        return is_match(w, p, i+1, j+1)

print get_words_matching_prefix(["cat", "dog","can","cut", "doll"], "ca")



