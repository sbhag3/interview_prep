class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        tokens, st, d = [''], [], {}
        def evaluate(tokens):
            if tokens[0] in ['add', 'mult']:
                n1, n2 = int(d.get(tokens[1], tokens[1])), int(d.get(tokens[2], tokens[2]))
                print(str(n1+n2) if tokens[0] == 'add' else str(n1*n2))
                return str(n1+n2) if tokens[0] == 'add' else str(n1*n2)
            else:
                for i in range(1, len(tokens)-2, 2): d[tokens[i]] = d.get(tokens[i+1], tokens[i+1])
                return d.get(tokens[-1], tokens[-1]) 
            
        for c in expression:
            if c == '(':
                if tokens[0] == 'let': evaluate(tokens)
                st.append((tokens, dict(d)))
                tokens = ['']
            elif c == ')':
                val = evaluate(tokens)
                tokens, d = st.pop()
                tokens[-1] += val
            elif c == ' ': tokens.append('')
            else: tokens[-1] += c
        return int(tokens[0])
        