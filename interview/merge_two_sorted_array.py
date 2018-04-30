def merge(arr1, m, arr2, n):
    while m > 0 and n > 0:
        if arr1[m-1] >= arr2[n-1]:
            arr1[m+n-1]= arr1[m-1]
            m = m - 1
        else:
            arr1[m + n - 1] = arr2[n - 1]
            n = n - 1
    if n > 0:
        arr1[:n] = arr2[:n]
    return arr1

assert merge([1,2,0,0],2, [0,1], 2) == [0,1,1,2]