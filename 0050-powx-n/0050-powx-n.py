class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow((x * x), n // 2)
        ans = half
        if n % 2 != 0:
            ans *= x

        return ans
        
        