'''
collatz conjecture
'''
hash = {}
def collatz(n):
    global hash
    if n in hash:
        return hash[n]
    if n == 1:
        return 0
    if n%2 == 0:
        x = 1 + collatz(n / 2)
    else:
        x = 1 + collatz(3*n+1)
    hash[n] = x
    return x

assert collatz(27) == 111