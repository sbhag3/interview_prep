# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if inorder:
            split = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[split])
            root.left = self.buildTree(preorder, inorder[:split])
            root.right = self.buildTree(preorder, inorder[split+1:])

            return root
        return None
        