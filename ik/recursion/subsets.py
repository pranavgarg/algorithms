def gen_subsets(arr, target):
    sets = [None] * len(arr)
    gen_subsets_so_far(arr, 0, sets, 0, target)

def gen_subsets_so_far(arr, idx, sets, j, target):
    if idx == len(arr):
        if target == 0:
            print sets
        return
    gen_subsets_so_far(arr, idx+1, sets, j, target)
    sets[j] = arr[idx]
    target -= arr[idx]
    gen_subsets_so_far(arr, idx + 1, sets, j+1, target)
    sets[j] = None

