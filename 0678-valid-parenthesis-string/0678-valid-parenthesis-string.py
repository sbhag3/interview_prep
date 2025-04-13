class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openC, closeC = 0, 0
        n = len(s) - 1

        for i in range(n + 1):
            if s[i] == '(' or s[i] == '*':
                openC += 1
            else:
                openC -= 1

            if s[n - i] == ')' or s[n - i] == '*':
                closeC += 1
            else:
                closeC -= 1

            if openC < 0 or closeC < 0:
                return False

        return True
        
        