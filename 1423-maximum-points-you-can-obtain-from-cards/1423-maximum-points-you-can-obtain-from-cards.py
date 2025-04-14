class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        left = k - 1
        right = n - 1

        total = sum(cardPoints[:k])
        ans = total

        for _ in range(k):
            total += (cardPoints[right] - cardPoints[left])
            ans = max(ans, total)
            left -= 1
            right -= 1
        return ans