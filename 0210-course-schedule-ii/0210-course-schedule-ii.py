class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        dq = deque([i for i in range(numCourses) if indegree[i] == 0])
        ans = []

        while dq:
            curr = dq.popleft()
            ans.append(curr)
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    dq.append(nbr)

        return ans if len(ans) == numCourses else []
        