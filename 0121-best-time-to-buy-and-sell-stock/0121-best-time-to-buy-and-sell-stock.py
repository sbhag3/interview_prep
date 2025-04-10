class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_point = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            sell_point = prices[i]
            if sell_point < buy_point:
                buy_point = sell_point
            elif sell_point - buy_point > ans:
                ans = sell_point - buy_point

        return ans

        