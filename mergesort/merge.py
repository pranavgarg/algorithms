# input = [[1, 3, 5, 6], [3, 4, 7], [-1, 2]]
# output = [-1, 1, 2, 3, 3, 4, 5, 6, 7]
'''
CASE1:
    #input = [[1, 3, 5, 6]]
    #output =
CASE2:
    #input = []
    #output = []

    So assumption is atleast one

    k arrays
    each with n elements
    time complexity: k*(4n)=> k(n) => kn
'''


def merge(arrays):
    l = len(arrays)
    if l < 1:
        return []
    output = arrays[0]
    for i in range(1, len(arrays) - 1):
        output = help_merge(output, i)
    return output


def help_merge(arr1, arr2):
    # len = arr => 2
    indx_arr1 = 0
    indx_arr2 = 0
    output = []
    while indx_arr1 < len(arr1) or indx_arr2 < len(arr2):  # this is correct
        if indx_arr1 < len(arr1) and indx_arr2 < len(arr2):
            if arr1[indx_arr1] < arr2[indx_arr2]:
                output.append(arr1[indx_arr1])
                indx_arr1 += 1
            else:
                output.append(arr2[indx_arr2])
                indx_arr2 += 1
        elif indx_arr2 >= len(arr2):
            output.append(arr1[indx_arr1])
            indx_arr1 += 1
        else:
            output.append(arr2[indx_arr2])
            indx_arr2 += 1
    return output


# assert help_merge([],[]) == []
# assert help_merge([],[1,2,3]) == [1,2,3]
# assert help_merge([2,4],[1, 3, 5, 6]) == [1,2,3,4,5,6]
# assert merge([]) == []
assert merge([[1, 2, 3]]) == [1, 2, 3]
assert merge([[1, 2, 3], [0, 5]]) == [0, 1, 2, 3, 5]