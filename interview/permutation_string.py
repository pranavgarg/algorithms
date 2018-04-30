'''
capitalPermutations(word) -
Given a string of letters,
return all the possible combinations of lower and uppercase letters of that word.


// input: "abc"
    // output: {"abc","Abc","aBc","abC","ABc","AbC","aBC","ABC"}

    000 abc
    001 abC
    010 aBc
'''


def capitalPermutations(word):
    l = len(word)
    output = [None for _ in xrange(2 ** l)]
    for i in xrange(l):
        capitalize_index = format(i, '#b')  # bin(i)[2:]
        out = []
        for j in xrange(len(capitalize_index)):
            if capitalize_index[j] == '1':
                out.append(word[j].upper())
            else:
                out.append(word[j])
        output.append(''.join(out))
    return output


# print capitalPermutations('abc')

print format(1, '#03b')  # bin(i)[2:]

print format(1, '#03b') #bin(i)[2:]
