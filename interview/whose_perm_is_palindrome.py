"""

Write an efficient function that checks whether
any permutation of an input string is a palindrome.
Assume the input string only contains lowercase letters.

Examples:
+ "civic" should return True
+ "ivicc" should return True
+ "civil" should return False
+ "livci" should return False

**Key to optimizing permutation problems is almost always a hash table and memoization.

"""

def permutation_of(word):
    if len(word) <= 1:
        yield word
    else:
        for p in permutation_of(word[1:]):
            for i in range(len(word)):
                yield p[:i] + word[:1] + p[i:]
    
def is_palindrome(word):
    if len(word) <= 0:
        return False
    
    if len(word) <= 2:
        return True

    for i, c in enumerate(word):
        if word[i] != word[len(word)-1-i]:
            return False

    return True

def whose_perm_is_palindrome(word):
    for p in permutation_of(word):
        if is_palindrome(p):
            memo[word] = True
            return True

    return False

if __name__ == '__main__':
    memo = {}

    assert whose_perm_is_palindrome('civic')
    assert whose_perm_is_palindrome('icvci')
    assert whose_perm_is_palindrome('ivicc')
    assert not whose_perm_is_palindrome('civil')
    assert not whose_perm_is_palindrome('livci')
    assert not whose_perm_is_palindrome('livici')

    
