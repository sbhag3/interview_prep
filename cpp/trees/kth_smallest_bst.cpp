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
    vector<int> vals_;
    int kthSmallest(TreeNode* root, int k) {
        tree_vals(root);
        sort(vals_.begin(), vals_.end());
        return vals_[k-1];
    }

    void tree_vals(TreeNode* node) {
        if (!node) return;
        vals_.push_back(node->val);
        tree_vals(node->left);
        tree_vals(node->right);
    }
};