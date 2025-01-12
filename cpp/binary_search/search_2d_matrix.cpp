class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        if (m == 0) return false;
        int start = 0, end = m*n - 1;
        while (start <= end) {
            int middle = (start + end) / 2;
            int i = middle / n, j = middle % n;
            if (matrix[i][j] == target) return true;
            else if (matrix[i][j] > target) {
                end = middle - 1;
            } else start = middle + 1;
        }
        return false;
    }
};