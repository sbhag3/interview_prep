class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> ans;
        for (auto curr_interval : intervals) {
            if (curr_interval[1] < newInterval[0]) ans.push_back(curr_interval);
            else if (newInterval[1] < curr_interval[0]) {
                ans.push_back(newInterval);
                newInterval = curr_interval;
            } else {
                newInterval[0] = min(newInterval[0], curr_interval[0]);
                newInterval[1] = max(newInterval[1], curr_interval[1]);
            }
        }
        ans.push_back(newInterval);
        return ans;
    }
};