class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # for each one that I encounter
        # run BFS/DFS to try to find the entire island
        # return # of times this is done
        def dfs(i, j):
            if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans

        
        