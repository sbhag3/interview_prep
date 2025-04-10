class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def bipartite(graph, start, color):
            q = deque()
            q.append(start)
            color[start] = 1

            while q:
                curr = q.popleft()
                for nbr in graph[curr]:
                    if color[nbr] == 0:
                        color[nbr] = 2 if color[curr] == 1 else 1
                        q.append(nbr)
                    elif color[nbr] == color[curr]:
                        return False

            return True

        v = len(graph)
        color = [0] * v

        for i in range(v):
            if color[i] == 0:
                if not bipartite(graph, i, color):
                    return False
        return True
        