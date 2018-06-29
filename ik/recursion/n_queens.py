'''
n queens problem
'''
def validate_config(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i]-arr[j]) == abs(i-j):
                return False
    return True

def gen_permutations(arr, i):
    if i == len(arr) -1:
        if validate_config(arr):
            print arr
        return
    for j in range(i, len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        gen_permutations(arr, i+1)
        arr[j], arr[i] = arr[i], arr[j]

gen_permutations([0,1,2,3], 0)


