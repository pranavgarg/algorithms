class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        returnList = []
        sets = [None] * len(candidates)
        self.permutations(candidates, 0, sets, 0, target, returnList)
        return [list(x) for x in set(tuple(x) for x in returnList)]


    def permutations(self, candidates, i, sets, j, target,returnList):
        if i == len(candidates):
            if target == 0:
                returnList.append(sorted(sets[:j]))
            return
        self.permutations(candidates, i + 1, sets, j, target,returnList)
        sets[j] = candidates[i]
        self.permutations(candidates, i + 1, sets, j+1, target-candidates[i],returnList)


s = Solution()
print s.combinationSum2([10,1,2,7,6,1,5],8)