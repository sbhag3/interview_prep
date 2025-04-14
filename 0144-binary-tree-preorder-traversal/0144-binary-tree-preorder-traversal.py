# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(root, ans):
            if root:
                ans.append(root.val)
                helper(root.left, ans)
                helper(root.right, ans)

        ans = []
        helper(root, ans)
        return ans
        