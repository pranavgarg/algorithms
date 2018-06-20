def binary_search(a, search, low, hi):
    if low > hi:
        return False

    mid = low + (hi-low)/2
    if a[mid] == search:
        return True
    elif a[mid] < search:
        return binary_search(a, search, mid+1, hi);
    else:
        return binary_search(a, search, low, mid-1);


assert (binary_search([10,20,30,45], 20, 0, 1) == True)
assert (binary_search([1], 1, 0, 0) == True)