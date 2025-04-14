class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        def topo_sort(edges, n):
            graph = [[] for _ in range(n + 1)]
            indegree = [0] * (n + 1)

            order = []

            for u, v in edges:
                graph[u].append(v)
                indegree[v] += 1

            q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
            while q:
                curr = q.popleft()
                order.append(curr)
                n -= 1
                for adj in graph[curr]:
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        q.append(adj)

            if n != 0:
                return []
            return order

        row_order = topo_sort(rowConditions, k)
        col_order = topo_sort(colConditions, k)   
        if not row_order or not col_order:
            return []

        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if row_order[i] == col_order[j]:
                    matrix[i][j] = row_order[i]
        return matrix