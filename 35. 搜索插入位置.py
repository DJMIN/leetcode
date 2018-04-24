class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, i in enumerate(nums):
            if target <= i:
                return index
        return len(nums)
