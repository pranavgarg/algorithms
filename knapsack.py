'''
You are given a maximum weight lets say in this case 10
and then a double dimension array of values and weight
for e.g. 
[5,4]
[3,2]
[10,8]
[4,8]
first column represents value and second column represents weight. 
So given the example the best solution will be [3,2] and [10,8] as
they fulfill the maximum_weight criteria of 10 and there value is 13
out of all the subsets. 
This approach is solved using dynamic programming specifically memotization 
where the invariant is if the weight is in the idle subset it should be in the idle subset -1 as well. 

More about this: http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
'''

def knapsack(two_dimension_array, max_weight):
    temp = [[0 for _ in range(max_weight+1)] for _ in range(len(two_dimension_array)+1)]
    n = len(two_dimension_array);

    for i in range(n+1):
        for j in range(max_weight+1):
            if i == 0 or j == 0:
                temp[i][j] = 0
            elif two_dimension_array[i-1][1] <= j:
                temp[i][j] = max(
                    two_dimension_array[i-1][0] + temp[i-1][j-two_dimension_array[i-1][1]],
                                 temp[i-1][j]
                )
            else:
                temp[i][j] = temp[i-1][j]
    return temp[n][max_weight]



maximum_weight = 10;
#2d_array[price][weight]
two_dimension_array = [[5,4],[3,2],[10,8],[4,8]]
expected_output = 13;
assert knapsack(two_dimension_array, maximum_weight) == expected_output




