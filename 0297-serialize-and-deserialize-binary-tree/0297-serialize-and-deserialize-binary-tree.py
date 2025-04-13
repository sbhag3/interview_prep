# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recurse(root, curr):
            if root is None:
                curr += 'None,'
            else:
                curr += str(root.val) + ','
                curr = recurse(root.left, curr)
                curr = recurse(root.right, curr)
            return curr
        return recurse(root, '')
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recurse(split_data):
            if split_data[0] == 'None':
                split_data.pop(0)
                return None
            root = TreeNode(split_data[0])
            split_data.pop(0)
            root.left = recurse(split_data)
            root.right = recurse(split_data)
            return root
        split_data = data.split(',')
        root = recurse(split_data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))