class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        idx_j = 0
        idx_s = 0
        output = 0
        while (idx_s < len(S) and idx_j < len(J)):
            if J[idx_j] == S[idx_s]:
                output += 1
                idx_s += 1
            elif J[idx_j] > S[idx_s]:
                idx_s += 1
            else:
                idx_j += 1
        return output


s = Solution()
print s.numJewelsInStones("aA", "aAAbbbb")