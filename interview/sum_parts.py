'''
sliding window problem
'''

def max_sum(ar, k):
    max_sum = 0
    l = len(ar)
    if l < k:
        return None
    for i in range(0, k):
        max_sum += ar[i]
    roll = max_sum
    for i in range(k,l):
        roll = roll - ar[i-k] + ar[i]
        max_sum = max(max_sum, roll)
    return max_sum

a = [1, 4, 2, 10, 2, 3, 1, 0, 20]
print max_sum(a, 4)
