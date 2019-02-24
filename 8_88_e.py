def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    min_idx = 0
    max_idx = m - 1
    while i < n:
        if nums2[i] == nums1[(min_idx + max_idx) // 2]:
            nums1.insert(nums2[i])
        if nums2[i] > nums1[(min_idx + max_idx) // 2]:
            min_idx = (min_idx + max_idx) // 2 + 1
        else:
            max_idx = (min_idx + max_idx) // 2 - 1
        i += 1
    return nums1