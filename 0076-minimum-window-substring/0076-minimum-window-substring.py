class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""

        count_T, window = {}, {}
        
        for c in t:
            if c in count_T:
                count_T[c] += 1
            else:
                count_T[c] = 1
        
        have, need = 0, len(count_T)
        left = 0
        ans = [-1, -1]
        size = float("inf")

        for right in range(len(s)):
            c = s[right]
            
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            
            if c in count_T and window[c] == count_T[c]:
                have += 1

            while have == need:
                if (right - left + 1) < size:
                    ans = [left, right]
                    size = right - left + 1
                tmp = s[left]
                window[tmp] -= 1
                if tmp in count_T and window[tmp] < count_T[tmp]:
                    have -= 1
                left += 1

        left, right = ans
        return s[left : right + 1] if size != float("inf") else ""
        
        