class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = len(nums)

        if i ==2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        p = 1
        while p < i:
            if nums[p-1] == nums[p]:
                nums.pop(p)
                i -= 1
            else:
                p += 1

        return len(nums)