/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int pval = p->val;
        int qval = q->val;
        TreeNode* node = root;
        while (node) {
            if (pval > node->val && qval > node->val) node = node->right;
            else if (pval < node->val && qval < node->val) node = node->left;
            else return node;
        }
        return nullptr;
    }
};