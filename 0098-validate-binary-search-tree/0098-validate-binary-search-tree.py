# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return check(node.right, node.val, high) and check(node.left, low, node.val)

        return check(root, -float('inf'), float('inf'))
        