class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_cnt, s_cnt = [0] * 26, [0] * 26
        ans = []

        for ch in p:
            p_cnt[ord(ch) - ord('a')] += 1

        for i in range(ns):
            s_cnt[ord(s[i]) - ord('a')] += 1
            if i >= np:
                s_cnt[ord(s[i - np]) - ord('a')] -= 1

            if p_cnt == s_cnt:
                ans.append(i - np + 1)

        return ans
        