def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index1, num1 in enumerate(nums):
        num2 = target - num1
        if (num2 in nums) and (num2 != num1):
            return [index1, nums.index(num2)]


print (twoSum([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74], 144))