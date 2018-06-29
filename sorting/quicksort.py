def swap(arr, a, b):
    """
    Swapping takes O(1) time and O(1) space
    """
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def partition(arr, L, R):
    """
    The heart of quicksort algorithm. This is a 2-way partitioning technique.

    * Chooses a pivot or partitioned element (there are several ways to do that)
    * As long as the value at arr[L] is less than the pivot value, keep scanning to the right
    * As long as the value at arr[R] is more than the pivot value, keep scanning to the left
    * When both loops finished (meaning L and R have found a swappable pair), if L <= R, then swap the values at L and R.
    * Move L to the right away from the left swapped element and R to the left away from the right swapped element.
    * Repeat the outer while loop if necessary, or
    * return L as the new partitioned index for next call.

    This takes O(n) time, since swapping is an O(1) constant time operation (and constant space)
    and L will have to move to the right on average n/2 time and R will have to move to the left n/2 time.
    """
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
    """
    Quicksort takes O(n log n) time.
    The divide and conquer part makes this a O(log n) process because each sublist is logarithmically
    roughly half the size of the previous one.
    The partitioning for every call takes O(n) time, so it is O(n * log n).
    """
    if (len(arr) <= 1):
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

