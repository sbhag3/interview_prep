class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue # same bomb
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    # bomb i detonates bomb j
                    graph[i].append(j)

        def bfs(i):
            queue = deque([i])
            visited = set([i])
            while queue:
                curr = queue.popleft()
                for nbr in graph[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)
            return len(visited)

        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        return ans

        