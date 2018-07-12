def no_of_subsets(arr,i, t):
    if t == 0:
        return 1
    if i == len(arr):
        return 0
    return no_of_subsets(arr, i+1, t) + no_of_subsets(arr, i+1, t - arr[i])

print no_of_subsets([1,2,3,-1],0,5)