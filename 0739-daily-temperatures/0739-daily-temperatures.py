class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        maxT = 0
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            currT = temperatures[i]
            if currT >= maxT:
                maxT = currT
                continue
            
            wait = 1
            while temperatures[i + wait] <= currT:
                wait += ans[i + wait]
            ans[i] = wait

        return ans