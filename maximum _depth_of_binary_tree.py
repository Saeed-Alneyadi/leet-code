# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0 # Return zero if @root is None
        else:
            left = self.maxDepth(root.left) # Calculate the maximum depth of the left node
            right = self.maxDepth(root.right) # Calculate the maximum depth of the right node

            if left <= right:
                return 1 + right # Depth of the right node incrmeneted by 1 is returned if the maximum depth of the right is greater than or equal to left
            else:
                return 1 + left # Depth of the left node incrmeneted by 1 is returned if the maximum depth of the right is less than to left
