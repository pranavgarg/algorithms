'''
Palindrome
'''
def isPalindrome(str, start, end):
    if start >= end:
        return True
    if str[start] == str[end]:
        return isPalindrome(str, start+1, end-1)
    else:
        return False

# str = 'was it in a car or a cat i saw'.replace(' ','')
# assert isPalindrome(str, 0 , len(str)-1) == False
#
# str = 'go hand a salami im a lasagna hog'.replace(' ','')
# assert isPalindrome(str, 0 , len(str)-1) == True

str = 'abba'
assert isPalindrome(str, 0, len(str)-1)== True