def number_of_swaps(array):
    count = 0
    n = len(array)

    # create dict with {key:element , value:index}
    arr_dict = {}
    for index, ele in enumerate(array):
        arr_dict[ele] = index

    # To keep track of visited elements (initalise False)
    visited = [False] * n

    # Sort the dictionary with the key(ele) value
    for ele, index in sorted(arr_dict.items(), key=lambda x: x[0]):

        # if ele already visited or if its already at correct place, ignore
        if visited[ele] or ele == index:
            continue

        # otherwise count the elements in present cycle
        cycle_count = 0
        i = ele
        while not visited[i]:
            # element visited now
            visited[i] = True

            # visit the ele at its index
            i = arr_dict[i]
            cycle_count += 1

        # add the cycle_count to count (cycle-1 always for the loop)
        count += cycle_count - 1

    return count

print number_of_swaps([8,3,11,4,6])
