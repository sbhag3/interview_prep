class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> edit(m + 1, vector<int>(n + 1));

        for (int j = 0; j <= n; j++) {
            edit[0][j] = j;
        }
        for (int i = 0; i <= m; i++) {
            edit[i][0] = i;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int insert_ = edit[i][j-1] + 1;
                int delete_ = edit[i-1][j] + 1;
                int replace_ = edit[i-1][j-1];
                if (word1[i-1] != word2[j-1]) {
                    replace_ += 1;
                }
                edit[i][j] = min({insert_, delete_, replace_});
            }
        }
        
        return edit[m][n];
    }
};