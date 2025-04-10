class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        mp = {}
        most_seen = 0
        ans = 0
        for right in range(len(s)):
            mp[s[right]] = mp.get(s[right], 0) + 1

            most_seen = max(most_seen, mp[s[right]])

            is_valid = ((right - left + 1) - most_seen <= k)

            if not is_valid:
                mp[s[left]] -= 1
                left += 1

            ans = right - left + 1

        return ans
            

        