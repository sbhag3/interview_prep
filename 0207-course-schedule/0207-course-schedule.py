class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # total courses need to take is numCourses

        # [[1, 0]] courses = 2
        # need to take course 0 to finish course 1

        # [[1, 0], [0, 1]]
        # can't because for first requirement
        # need to take course 0 to finish course 1
        # but for second requirement
        # need to take course 1 to finish course 0
        # cyclic dependency

        # courses that we can do first
        # represent the course dependencies as a graph

        # we see that the courses we can take initially are the courses with indegree 0
        # in this case, we can also see that as we start to finish these courses, there
        # may be courses that also start to open up because all the prereqs are done

        # topological traversal of the graph

        # start with all nodes of indegree 0
        # start to "remove" them from the graph
        # if new nodes start to acquire an indegree of 0
        # we iterate on those
        # finally we see if the number of nodes we removed is exactly the number of courses
        # needed to be taken

        # time complexity: O(m + n), where m is the size of prereqs and n is numCourses
        # space complexity: O(m + n), graph is O(m) space and indegree is O(n) space

        # code:
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        taken = 0
        while queue:
            curr = queue.popleft()
            taken += 1
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)

        return taken == numCourses