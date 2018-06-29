
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.gen_permutations(nums, 0)


    def gen_permutations(self, nums, i, output=[]):
        if i == len(nums) - 1:
            output.append(nums[:])
            return output
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.gen_permutations(nums, i+1, output)
            nums[i], nums[j] = nums[j], nums[i]
        return output
s = Solution()

print s.permute([1,2])