class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def countPalindromes(s, i, j):
            ans = 0

            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
                ans += 1
            return ans

        ans = 0
        for i in range(len(s)):
            ans += countPalindromes(s, i, i)
            ans += countPalindromes(s, i, i+1)

        return ans
        