class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return [] # empty rooms

        m, n = len(rooms), len(rooms[0])
        q = deque() # BFS implementation
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j)) # find all gates first

        while q: 
            x, y = q.popleft() # go thru each gate and populate empty rooms w distance
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in dirs:
                newX, newY = x + dx, y + dy
                if newX >= 0 and newX < m and newY >= 0 and newY < n and rooms[newX][newY] > rooms[x][y]:
                    rooms[newX][newY] = rooms[x][y] + 1
                    q.append((newX, newY)) # push filled room into queue for search to continue