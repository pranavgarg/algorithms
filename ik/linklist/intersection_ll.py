def find_intersection(l1, l2):
    big = None
    small = None
    i = l1
    j = l2
    ahead = 0
    while i or j:
        if i is not None and j is not None:
            i = i.next
            j = j.next
        elif i is not None:
            ahead += 1
            big = l1
            small = l2
            i = i.next
        else:
            ahead += 1
            big = l2
            small = l1

    for i in range(ahead):
        # move ahead
        big = big.next
    while big and small:
        if big == small:
            return big.val
        else:
            big = big.next
            small = small.next
    return -1