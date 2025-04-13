class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        ans = 0
        edges = 0

        in_tree = [False] * n

        min_dist = [float("inf")] * n
        min_dist[0] = 0

        while edges < n:
            curr_edge = float("inf")
            curr_node = -1

            for node in range(n):
                if not in_tree[node] and curr_edge > min_dist[node]:
                    curr_edge = min_dist[node]
                    curr_node = node

            ans += curr_edge
            edges += 1
            in_tree[curr_node] = True

            for adj in range(n):
                weight = abs(points[curr_node][0] - points[adj][0]) + abs(points[curr_node][1] - points[adj][1])
                if not in_tree[adj] and min_dist[adj] > weight:
                    min_dist[adj] = weight

        return ans
        