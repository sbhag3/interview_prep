class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        taken = 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            curr = queue.popleft()
            taken += 1
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)

        return taken == numCourses
        