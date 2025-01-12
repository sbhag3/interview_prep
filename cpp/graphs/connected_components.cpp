class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        if (n == 0) return 0;
        int ans = 0;
        vector<bool> visited(n, false);
        vector<int> adj[n];
        for (int i = 0; i < edges.size(); i++) {
            adj[edges[i][0]].push_back(edges[i][1]);
            adj[edges[i][1]].push_back(edges[i][0]);
        }
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                ans++;
                search(adj, visited, i);
            }
        }
        return ans;
    }

    void search(vector<int> adj[], vector<bool>& visited, int source) {
        visited[source] = true;
        for (int i = 0; i < adj[source].size(); i++) {
            if (!visited[adj[source][i]]) {
                search(adj, visited, adj[source][i]);
            }
        }
    }
};