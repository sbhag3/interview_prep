class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        chains_seen = {}
        ans = 1
        for word in sorted(words, key=len):
            chains_seen[word] = 1
            for i in range(len(word)):
                drop_one = word[:i] + word[i + 1:]
                if drop_one in chains_seen:
                    chains_seen[word] = max(chains_seen[word], chains_seen[drop_one] + 1)
                    ans = max(ans, chains_seen[word])

        return ans