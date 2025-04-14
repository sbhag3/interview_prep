class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) < n - 1:
            return -1

        trust_score = [0] * (n + 1)

        for a, b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1

        for i, score in enumerate(trust_score[1:], 1):
            if score == n - 1:
                return i
        return -1
        