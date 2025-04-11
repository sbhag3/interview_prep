# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []

        def dfs(node, level):
            if level == len(ans):
                ans.append(node.val)
            if node.right:
                dfs(node.right, level + 1)
            if node.left:
                dfs(node.left, level + 1)

        dfs(root, 0)
        return ans
        