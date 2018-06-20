'''
print all substrings of a given string
'''
import timeit
from time import time
def all_substrings(str):
    l = len(str)
    substrings = []
    for i in range(0,l):
        for j in range(i+1,l+1):
            temp = []
            for k in range(i, j):
                temp.append(str[k])
            substrings.append(''.join(temp))
    return substrings

print all_substrings("aba")
start = time()
timeit.repeat('all_substrings("abcdefghijklmnofpeqrstuvwxyzda")',setup="from __main__ import all_substrings",number= 100)
end = time()
print end - start