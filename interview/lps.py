'''
length of longest palindrome subsequence
'''
def lps(instring, i,j):
    if i==j:
        return 1
    if instring[i]==instring[j] and i+1==j:
        return 2
    if instring[i]==instring[j]:
        return lps(instring,i+1,j-1) + 2
    return max(lps(instring,i+1,j),lps(instring,i,j-1))

assert lps("radar",0,4)==5
assert lps("geeksforgeeks",0,12)==5
