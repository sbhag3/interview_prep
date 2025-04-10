class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def fill(left, right, curr):
            if len(curr) == n * 2:
                ans.append(curr)
                return

            if left < n:
                fill(left + 1, right, curr + "(")
            
            if right < left:
                fill(left, right + 1, curr + ")")

        fill(0, 0, "")
        return ans
