def max_sub_array(nums):
    sum, ret = 0, nums[0]
    for num in nums:
        sum = max(sum + num, num)
        ret = max(sum, ret)
    return ret

print(max_sub_array([-1,2,3,-4,3,-3]))