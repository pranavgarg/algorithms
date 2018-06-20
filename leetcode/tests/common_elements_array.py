# Implement your function below.
def common_elements(list1, list2):
    il1 = 0
    l_l1 = len(list1)
    il2 = 0
    l_l2 = len(list2)
    result = []
    while (il1 < l_l1 and il2 < l_l2):
        if list1[il1] == list2[il2]:
            result.append(list1[il1])
            il1 = il1+1
            il2 = il2 + 1 
        elif list1[il1] > list2[il2]:
            il2 +=1
        else:
            il1+=1
    return result



# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
assert common_elements(list_a1, list_a2) == [1, 4, 9]

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
assert common_elements(list_b1, list_b2)== [1, 2, 9, 10, 12]

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
assert common_elements(list_c1, list_c2) == []