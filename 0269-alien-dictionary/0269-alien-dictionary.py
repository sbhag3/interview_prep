class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        # basic idea: construct a graph where ordering of letters is preserved
        # i.e., for words "wrt" and "wrf", both the first letters are the same
        # but t comes before f in this dictionary, so t -> f in our graph

        # after creating the graph, we do a topological ordering of the nodes
        # this will give us the answer

        if len(words) == 0:
            return ""

        ans = []
        graph = {}
        indegrees = {}

        for word in words:
            for letter in word:
                indegrees[letter] = 0
                graph[letter] = []

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            smaller = min(len(first), len(second))
            for j in range(smaller):
                parent, child = first[j], second[j]
                if parent != child:
                    graph[parent].append(child)
                    indegrees[child] += 1
                    break
                elif j == smaller - 1:
                    if len(second) < len(first):
                        return ""

        source_nodes = deque()
        for letter in indegrees:
            if indegrees[letter] == 0:
                source_nodes.append(letter)

        while source_nodes:
            curr = source_nodes.popleft()
            ans.append(curr)
            for child in graph[curr]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    source_nodes.append(child)

        return "" if len(indegrees) != len(ans) else "".join(ans)
        