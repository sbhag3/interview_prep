class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # my name is Shashank
        # k = 2
        # my name

        # iterate through character in the string

        # once i find a space, ik that means we are at the end of a word

        # "my name"
        # my name is Shashank
        #        .
        # count = 2
        # k = 2
        # count == k

        count = 0
        ans = ""

        for ch in s:
            if ch == ' ':
                count += 1
                if count == k:
                    return ans
            ans += ch

        return ans