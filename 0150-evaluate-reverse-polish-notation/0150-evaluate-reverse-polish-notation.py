class Solution:
    def evalRPN(self, tokens):
        st = []

        for t in tokens:
            if t not in "+-*/":
                st.append(int(t))
                continue

            number2 = st.pop()
            number1 = st.pop()

            curr = 0

            if t == "+":
                curr = number1 + number2
            elif t == "-":
                curr = number1 - number2
            elif t == "*":
                curr = number1 * number2
            else:
                curr = int(float(number1) / float(number2))

            st.append(curr)

        return st.pop()

        