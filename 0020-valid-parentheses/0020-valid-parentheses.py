class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []

        pairs = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pairs:
                top = st.pop() if st else "#"
                if pairs[c] != top:
                    return False
            else:
                st.append(c)

        return not st
        