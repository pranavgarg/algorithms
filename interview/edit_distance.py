'''
str1 = "dog", str2 = "frog"
edit distance should print 3
'''

def edit_distance(str1, str2):
    memo = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for idx1 in range(1, len(str1)+1):
        for idx2 in range(1, len(str2)+1):
            if str1[idx1-1] == str2[idx2-1]:
                memo[idx1][idx2] = memo[idx1-1][idx2-1]
            else:
                memo[idx1][idx2] = 1+ min(memo[idx1 - 1][idx2],memo[idx1][idx2-1])
    return memo[len(str1)][len(str2)]

print edit_distance("dog", "frog")