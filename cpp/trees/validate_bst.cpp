/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool helper(TreeNode* root, TreeNode* least, TreeNode* most) {
        if (!root) return true;
        if ((least && least->val >= root->val) || (most && most->val <= root->val)) return false;
        return helper(root->right, root, most) && helper(root->left, least, root);
    }

    bool isValidBST(TreeNode* root) {
        return helper(root, NULL, NULL);
    }
};