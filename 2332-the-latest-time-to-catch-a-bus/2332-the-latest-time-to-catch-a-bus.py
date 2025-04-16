class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        passengers.sort()
        cur = 0

        for time in sorted(buses):
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1

        best = time if cap > 0 else passengers[cur - 1]

        passengers = set(passengers)
        while best in passengers:
            best -= 1
        return best
        