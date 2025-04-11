# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, float("-inf"))] # keeping track of current node and current max
        ans = 0

        while stack:
            node, curr_max = stack.pop()
            if curr_max <= node.val:
                ans += 1
            if node.left:
                stack.append((node.left, max(node.val, curr_max)))
            if node.right:
                stack.append((node.right, max(node.val, curr_max)))

        return ans
        