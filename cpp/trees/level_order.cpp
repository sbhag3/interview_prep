class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        if (root == NULL) return levels;
        deque<TreeNode*> queue;
        queue.push_back(root);
        int level = 0;
        while (!queue.empty()) {
            levels.push_back({});
            int level_length = queue.size();
            for (int i = 0; i < level_length; ++i) {
                TreeNode* node = queue.front();
                queue.pop_front();
                levels[level].push_back(node->val);
                if (node->left != NULL) queue.push_back(node->left);
                if (node->right != NULL) queue.push_back(node->right);
            }
            level++;
        }
        return levels;
    }
};