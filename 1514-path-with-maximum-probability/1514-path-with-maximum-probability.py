class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))


        max_prob = [0.0] * n
        pq = [(-1.0, start_node)]
        while pq:
            prob, node = heapq.heappop(pq)
            if node == end_node:
                return -prob

            if graph[node]:
                for adj, edge_prob in graph[node]:
                    if -prob * edge_prob > max_prob[adj]:
                        max_prob[adj] = -prob * edge_prob
                        heapq.heappush(pq, (-max_prob[adj], adj))
                graph[node] = []

        return 0.0
        