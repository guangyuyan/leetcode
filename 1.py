def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    while i < len(nums) - 1:
        j = i + 1
        while j < len(nums):
            if target == nums[i] + nums[j]:
                ls = [i, j]
                return ls
                break
            j = j + 1
        i = i + 1

"""
test case:
nums = [2, 7, 11, 15], target = 9
"""