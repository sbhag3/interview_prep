class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int count = 0;
        if (numCourses <= 0) return true;

        vector<int> indegree(numCourses, 0);
        vector<vector<int>> graph(numCourses);

        for (auto& edge : prerequisites) {
            int parent = edge[1];
            int child = edge[0];
            graph[parent].push_back(child);
            indegree[child]++;
        }

        queue<int> sources;

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) sources.push(i);
        }

        while (!sources.empty()) {
            int curr = sources.front(); sources.pop();
            count++;
            for (int child : graph[curr]) {
                indegree[child]--;
                if (indegree[child] == 0) sources.push(child);
            }
        }
        return count == numCourses;
    }
};