def mergesort(arr):
    if (len(arr) <= 1):
        return arr

    left, right = half(arr)
    L = mergesort(left)
    R = mergesort(right)

    return merge(L, R)

def merge(a, b):
    """
    Merges two contending lists by picking either head
    element of either list which is lesser than or equal
    to the other and append it to the output list and remove the
    element from the list. After the either list is empty,
    it exhausts the leftover list and append all its element
    to the outputting list.
    
    ================
    Time complexity:
    ================

    The first `while` loop will work with approximately `len(a) + len(b) / 2`
    elements in average cases when `len(a)` and `len(b)` are roughly comparable.
    That's O(a + b / 2) or O(N).

    Appending to a list is an O(1) operation, so O(N + 1) stays O(N).

    Either the second or third `while` loop will be called, and in average cases
    the leftover list should contains around N / 2 elements so this will incur
    O(N / 2) work for moving each element to the outputting list until empty, which
    is roughly O(N).

    The totally time complexity is O(N).

    =================
    Space complexity:
    =================

    This improved solution sacrifices little memory by storing counters for two lists
    and increment them in order to correctly access the current element without ever
    removing the head element in mergesort.py. It only takes O(1) space to store them.

    """

    out = []

    ai = 0
    bi = 0
    
    while (ai <= len(a) - 1 and bi <= len(b) - 1):
        if (a[ai] <= b[bi]):
            out.append(a[ai])
            ai += 1
        else:
            out.append(b[bi])
            bi += 1

    while (ai <= len(a) - 1):
        out.append(a[ai])
        ai += 1

    while (bi <= len(b) - 1):
        out.append(b[bi])
        bi += 1

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
