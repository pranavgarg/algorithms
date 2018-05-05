def mergesort(arr):
    if (len(arr) <= 1):
        return arr

    left, right = half(arr)
    L = mergesort(left)
    R = mergesort(right)

    return merge(L, R)

def merge(a, b):
    out = []

    while (len(a) > 0 and len(b) > 0):
        if (a[0] <= b[0]):
            out.append(a[0])
            del a[0]
        else:
            out.append(b[0])
            del b[0]

    while (len(a) > 0):
        out.append(a[0])
        del a[0]

    while (len(b) > 0):
        out.append(b[0])
        del b[0]

    return out

def half(arr):
    mid = len(arr) / 2
    return arr[:mid], arr[mid:]

if __name__ == "__main__":
    assert(merge([1], [2]) == [1, 2])
    assert(merge([2], [1]) == [1, 2])
    assert(merge([2, 3], [1, 2]) == [1, 2, 2, 3])
    assert(merge([2, 3, 0], [1, 2, 16, 32, 1]) == [1, 2, 2, 3, 0, 16, 32, 1])

    assert(half([0, 1, 2, 3, 4]) == ([0, 1], [2, 3, 4]))
    assert(half([1, 2, 3, 4]) == ([1, 2], [3, 4]))
    assert(half([]) == ([], []))
    assert(half([1]) == ([], [1]))

    assert(mergesort([]) == [])
    assert(mergesort([1]) == [1])
    assert(mergesort([5, 2, 0, 2, 8, 7]) == [0, 2, 2, 5, 7, 8])
    assert(mergesort([0, 1, 2, 3, 6, 5]) == [0, 1, 2, 3, 5, 6])
