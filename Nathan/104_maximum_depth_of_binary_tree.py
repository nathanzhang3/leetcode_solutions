# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return self.lookDeeper(root.left, root.right, 1)
        
    def lookDeeper(self, left, right, depth):
        leftLen = rightLen = depth
        if left is not None:
            leftLen += self.lookDeeper(left.left, left.right, depth)
        if right is not None:
            rightLen += self.lookDeeper(right.left, right.right, depth)
        
        return max(leftLen, rightLen)