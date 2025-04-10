class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n <= 0:
            return 0

        if n == 1:
            return 1

        parent = [i for i in range(n)]
        size = [1 for i in range(n)]

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

        for u, v in edges:
            if union(u, v):
                n -= 1

        return n

        
        