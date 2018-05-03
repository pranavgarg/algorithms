class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx, c in enumerate(nums):
            nums[idx] = -nums[idx]
        print nums
s = Solution()
s.findDisappearedNumbers([4,3,2,7,8,2,3,1])