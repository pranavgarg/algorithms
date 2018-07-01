def swap(arr, L, R):
    tmp = arr[L]
    arr[L] = arr[R]
    arr[R] = tmp
    return arr

def sort(arr):
    for i, _ in enumerate(arr):
	k = i
 	while (k > 0 and arr[k] < arr[k-1]):
	      arr = swap(arr, k-1, k)
	      k -= 1
	      
    return arr

if __name__ == "__main__":
    assert(swap([0, 2], 0, 1) == [2, 0])
    assert(swap([4, 3], 0, 1) == [3, 4])
    assert(swap([4, 2, 0, 1], 1, 3) == [4, 1, 0, 2])
    
    assert(sort([0]) == [0])
    assert(sort([10]) == [10])
    assert(sort([0, 2, 1, 3, 1]) == sorted([0, 2, 1, 3, 1]))		
    assert(sort([4, 3, 60, 12, 43, 2]) == sorted([4, 3, 60, 12, 43, 2]))
