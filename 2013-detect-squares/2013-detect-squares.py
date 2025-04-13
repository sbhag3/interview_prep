class DetectSquares(object):

    def __init__(self):
        self.mp = {}
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        if tuple(point) not in self.mp:
            self.mp[tuple(point)] = 0
        self.mp[tuple(point)] += 1
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        ans = 0
        px, py = point
        for x, y in self.mp.keys():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if (x, py) in self.mp and (px, y) in self.mp:
                ans += self.mp[(x, py)] * self.mp[(px, y)] * self.mp[(x, y)]
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)