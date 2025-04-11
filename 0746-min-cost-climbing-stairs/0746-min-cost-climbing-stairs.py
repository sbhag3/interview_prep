class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        one = two = 0
        for i in range(2, len(cost) + 1):
            tmp = one
            one = min(one + cost[i - 1], two + cost[i - 2])
            two = tmp
        return one
        