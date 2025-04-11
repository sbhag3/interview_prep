class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp[i] = true if a1 to ai is a string in dict
        n = len(s)
        dp = [False] * (n + 1)
        word_set = set(wordDict)
        dp[0] = True

        for i in range(1, n + 1):
            dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))

        return dp[n]
        