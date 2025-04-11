# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans

        level = 0
        queue = deque([root])

        while queue:
            ans.append([]) # adding a level to the ans
            size_of_level = len(queue) # queue will always have # nodes at each level
            for i in range(size_of_level):
                curr = queue.popleft()
                ans[level].append(curr.val) # adding the current node to the level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

        return ans
        