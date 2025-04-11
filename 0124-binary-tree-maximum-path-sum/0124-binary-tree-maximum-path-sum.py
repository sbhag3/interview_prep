# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.curr = -float("inf")

        def helper(node):
            if not node:
                return 0

            left_sum = max(helper(node.left), 0)
            right_sum = max(helper(node.right), 0)

            self.curr = max(self.curr, left_sum + right_sum + node.val)

            return max(left_sum + node.val, right_sum + node.val)

        helper(root)
        return self.curr        