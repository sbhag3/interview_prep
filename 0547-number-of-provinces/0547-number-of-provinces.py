class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            parent[rootX] = rootY
            return True

        ans = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] and find(i) != find(j):
                    ans -= 1
                    union(i, j)

        return ans
        