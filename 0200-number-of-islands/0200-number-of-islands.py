class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        def dfs(i, j, grid):
            if (
                i < 0 or j < 0 
                or i >= len(grid) or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            
            grid[i][j] = 0
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    ans += 1
                    
        return ans
        