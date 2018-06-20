'''

Merge First Sorted Array Into Second Sorted Array

Problem Statement:

Given two arrays sorted in increasing order:

1) arr1 of size n which contains n positive integers sorted in increasing order.
2) arr2 of size 2n (twice the size of first) which also contains n positive integers sorted in increasing order in its first half. Second half of this array is empty. (Empty elements are marked by 0).

Write a function that takes these two arrays, and merges the first one into second one, resulting in one fully increasingly sorted array of 2n positive integers.

Input Format:

There are two arguments. First one is an integer array denoting arr1 of size n and second one is also an integer array denoting arr2 of size 2n.

Output Format:

Return arr2 containing 2n increasingly sorted positive integers.

Constraints:

1 <= n <= 10^5
1 <= arr1[i] <= 2 * 10^9
1 <= arr2[i] <= 2 * 10^9 (for the first half)
arr2[i] = 0 (for the second half)
You can use only constant extra space.
0 denotes an empty space.

Sample Test Case:

Sample Input:

n = 3
arr1 = [1 3 5]
arr2 = [2 4 6 0 0 0]

Sample Output:

arr2 = [1 2 3 4 5 6]
'''


def merger_first_into_second(arr1, arr2):
    #
    # Write your code here.
    #
    l = len(arr1)
    for idx, element in enumerate(arr1):
        arr2[l + idx] = element
    return sorted(arr2)



if __name__ == "__main__":
    fptr = sys.stdout

    arr1_count = int(input())

    arr1 = []

    for _ in range(arr1_count):
        arr1_item = int(input())
        arr1.append(arr1_item)

    arr2_count = int(input())

    arr2 = []

    for _ in range(arr2_count):
        arr2_item = int(input())
        arr2.append(arr2_item)

    res = merger_first_into_second(arr1, arr2)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

