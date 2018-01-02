class Solution:
    def sliding_window(self, inp_string):
        l = len(inp_string);
        s = set()
        ans,i,j = 0,0,0
        while (i < l and j < l):
            if (inp_string[j] not in s):
                s.add(inp_string[j])
                j +=1
                ans = max(ans, j-i)
            else:
                s.remove(inp_string[i])
                i+=1
        return ans

s = Solution()
assert s.sliding_window("abcabc") == 3

