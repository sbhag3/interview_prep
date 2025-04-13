class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans, power = 0, 31
        while n:
            ans += (n & 1) << power
            n = n >> 1
            power -= 1
        return ans
        