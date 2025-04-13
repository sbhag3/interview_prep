class UF:
    def __init__(self, n):
        self.components = n
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return 0
        if self.size[rootX] > self.size[rootY]:
            self.size[rootX] += self.size[rootY]
            self.parent[rootY] = rootX
        else:
            self.size[rootY] += self.size[rootX]
            self.parent[rootX] = rootY
        self.components -= 1
        return 1

    def connected(self):
        return self.components == 1

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        alice, bob = UF(n), UF(n)


        req_edges = 0
        for kind, u, v in edges:
            if kind == 3:
                req_edges += (alice.union(u, v) | bob.union(u, v))

        for kind, u, v in edges:
            if kind == 1:
                req_edges += alice.union(u, v)
            elif kind == 2:
                req_edges += bob.union(u, v)

        if alice.connected() and bob.connected():
            return len(edges) - req_edges

        return -1

        

                