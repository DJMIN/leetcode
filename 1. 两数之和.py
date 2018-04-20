class Solution:
    def twoSum(self, nums, target):
        for index1, num1 in enumerate(nums):
            num2 = target - num1
            if (num2 in nums) and (index1 != nums.index(num2)):
                return [index1, nums.index(num2)]
