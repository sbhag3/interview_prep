# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_val, q_val = p.val, q.val

        trav = root

        while trav:
            parent_val = trav.val
            if p_val > parent_val and q_val > parent_val:
                # LCA is in right subtree
                trav = trav.right
            elif p_val < parent_val and q_val < parent_val:
                # LCA is in left subtree
                trav = trav.left
            else:
                # LCA is the current node
                return trav
        