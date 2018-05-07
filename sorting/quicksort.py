def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def partition(arr, L, R):
    pivot = arr[len(arr) / 2]
    while (L <= R):
        while(arr[L] < pivot):
            L += 1
        while(arr[R] > pivot):
            R -= 1
        if (L <= R):
            swap(arr, L, R)
            L += 1
            R -= 1
    return L

def quicksort(arr):
    if (len(arr) <= 1):
        return arr
    elif (len(arr) == 2):
        if (arr[0] < arr[1]):
            return arr

    for i, _ in enumerate(arr):
        if (i == len(arr) - 1):
            break
        if (arr[i] > arr[i+1]):
            L = partition(arr, 0, len(arr) - 1)
            return quicksort(arr[:L]) + quicksort(arr[L:])
        
    return arr

if __name__ == "__main__":
    a = [4, 2, 6, 5, 3, 9]
    b = [4, 3, 2, 2, 1, 0]
    c = [2, 0, 0, 8, 8]
    d = [1, 2, 5, 4, 5, 2, 8, 1]

    a_ = quicksort(a)
    b_ = quicksort(b)
    c_ = quicksort(c)
    d_ = quicksort(d)

    assert(a_ == sorted(a))
    assert(b_ == sorted(b))
    assert(c_ == sorted(c))
    assert(d_ == sorted(d))

