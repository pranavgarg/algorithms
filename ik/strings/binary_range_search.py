'''
binary range search
'''

def binary_range_search(s,t):
    l = len(s)
    first = find_occurence(s, t, 0, l-1, True)
    last = find_occurence(s, t, 0, l-1, False)
    if first == -1 or last == -1:
        return -1
    return last - first + 1


def find_occurence(s, t, low, high, first_occurence):
    result = -1
    while (low <= high):
        mid = low + (high-low)/2
        if s[mid] == t:
            if first_occurence:
                high = mid -1
            else:
                low = mid + 1
            result = mid
        elif t < s[mid]:
            high = mid -1
        else:
            low = mid + 1

    if result != -1:
        return result
    return -1

assert binary_range_search("abbbcd","k") == -1
assert binary_range_search("abbbcd","b") == 3