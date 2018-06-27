def gen_permutations(arr):
    if type(arr) == "string":
        arr = list(arr)
    permutations(arr, 0)

def permutations(arr, i):
    if i == len(arr)-1:
        print arr
        return
    for j in range(i, len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        permutations(arr, i+1)
        arr[j], arr[i] = arr[i], arr[j]

#gen_permutations("abc")
gen_permutations([0,1,2])