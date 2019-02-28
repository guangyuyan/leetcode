def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 1:
        return [nums]
    results = []
    for index in range(len(nums)):
        for item in permute(nums[:index] + nums[index + 1:]):
            results.append([nums[index]] + item)

    return results