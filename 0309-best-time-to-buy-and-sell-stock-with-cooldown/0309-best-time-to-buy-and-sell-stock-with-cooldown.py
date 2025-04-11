class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold, held, reset = float("-inf"), float("-inf"), 0

        for price in prices:
            pre_sold = sold
            sold = held + price

            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)
        