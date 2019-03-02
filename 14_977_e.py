def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    return sorted(x * x for x in A)
