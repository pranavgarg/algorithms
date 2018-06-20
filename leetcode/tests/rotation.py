# Implement your function below.
def is_rotation(list1, list2):
    l1 = len(list1)
    l2 = len(list2)
    if l1 != l2:
        return False
    idx = 0
    point = -1
    for i,e in enumerate(list2):
        if list1[idx] == e:
            if point == -1 :
                point = i
            idx+=1

    for i in list2[:point]:
        if list1[idx] == i:
            idx += 1
    if idx == l1:
        return True
    else:
        return False




# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
assert is_rotation(list1, list2a) == True
list1 = [1]
list2 = [2]
assert is_rotation(list1, list2a) == False