class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def fp(node, parent):
            if (node == parent[node]):
                return node
            return fp(parent[node], parent)

        n = len(edges) + 1
        ans = []
        par = []
        for i in range(n):
            par.append(i)
        for edge in edges:
            tmp1 = fp(edge[0], par)
            tmp2 = fp(edge[1], par)
            if tmp1 == tmp2:
                ans = [edge[0], edge[1]]
            else:
                par[tmp2] = tmp1

        return ans
