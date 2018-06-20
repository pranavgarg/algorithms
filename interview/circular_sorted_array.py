def find_element(arr, find, low, high):
    mid = low + (high-low)/2
    if low <=mid:

        if arr[mid] == find:
            return True
        else:

    elif arr[mid] <= arr[high]:
        if arr[mid] < find and find <= arr[high]:
            return find_element(arr, find, mid+1, high)
        else:
            return find_element(arr, find, low, mid-1)
    elif arr[mid] >= arr[low]:
        if arr[mid] > find and find >= arr[low]:
            return find_element(arr, find, low, mid-1)
        else:
            return find_element(arr, find, mid+1, high)
    else:
        return False

print (find_element([10,1,2,3], 10, 0, 4))