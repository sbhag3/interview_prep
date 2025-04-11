class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w

        heap = [(0, src, k + 1)]
        visited = [0] * n

        while heap:
            w, x, k = heapq.heappop(heap)
            if x == dst:
                return w
            if visited[x] >= k:
                continue
            visited[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(heap, (w + dw, y, k - 1))
        return -1
        