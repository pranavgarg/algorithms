def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(more)


if __name__ == '__main__':
    a = [3, 2, 0, 1]
    b = [0, 1, 8, 2, 0, 2, 10, 5]
    c = []
    d = [8,0]
    e = [0, 1, 1, 8, 8, 4, 3, 2, 2]

    assert(quicksort(a) == sorted(a))
    assert(quicksort(b) == sorted(b))
    assert(quicksort(c) == sorted(c))
    assert(quicksort(d) == sorted(d))
    assert(quicksort(e) == sorted(e))
    
