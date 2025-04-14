"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def helper(root, ans):
            if not root:
                return 
            
            for child in root.children:
                helper(child, ans)

            ans.append(root.val)

        ans = []
        helper(root, ans)
        return ans
        