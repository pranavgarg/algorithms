class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx, idxn = 0, 0
        if not needle:
            return 0
        while (idx < len(haystack)):
            if haystack[idx] == needle[idxn]:
                idxn +=1
                if idxn == len(needle):
                    return idx+1 - idxn
            elif idxn > 0:
                idx = idx - idxn
                idxn = 0
            idx +=1
        return -1


s = Solution();
print s.strStr("mississippi", "issip")
#print s.strStr("mississippi","pi")