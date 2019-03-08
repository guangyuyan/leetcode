def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

print(maxDepth([3,9,20,3,2,15,7,3,4,5,6,7,8,9,0,1,2,4,5,6]))