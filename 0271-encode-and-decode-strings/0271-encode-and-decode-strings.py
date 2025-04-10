class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        for s in strs:
            ans += s.replace('/', '//') + '/:'
        return ans

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ans = []
        curr = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == '/:':
                ans.append(curr)
                curr = ""
                i += 2
            elif s[i:i+2] == '//':
                curr += '/'
                i += 2
            else:
                curr += s[i]
                i += 1

        return ans
        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))