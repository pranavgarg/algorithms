'''
binary search using recursion
'''

def binary_search(s,t):
    l = len(s)-1
    print find(s,t,0,l)

def find(s,t, start, end):
    if start > end:
        return -1
    mid = start + (end - start) / 2
    if s[mid] == t:
        return mid
    elif t < s[mid]:
        return find(s, t, start, mid-1)
    else:
        return find(s, t, mid+1, end)

assert binary_search("abcd","k") == -1
assert binary_search("abcd","a") == 0
