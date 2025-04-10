class TimeMap(object):

    def __init__(self):
        self.mp = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if not key in self.mp:
            self.mp[key] = []
        self.mp[key].append([timestamp, value])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not key in self.mp:
            return ""

        if timestamp < self.mp[key][0][0]:
            return ""

        left, right = 0, len(self.mp[key]) 
        while left < right:
            mid = (left + right) // 2
            if self.mp[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return "" if right == 0 else self.mp[key][right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)