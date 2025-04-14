class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        def dfs(graph, visited, src, target):
            visited[src] = True
            if src == target:
                return True

            for nbr in graph[src]:
                if not visited[nbr]:
                    if dfs(graph, visited, nbr, target):
                        return True

            return False

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        ans = []

        for src, dest in queries:
            visited = [False] * numCourses
            ans.append(dfs(graph, visited, src, dest))

        return ans