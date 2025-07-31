class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+', '-', '*', '/'}
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                t2 = stack.pop()
                t1 = stack.pop()
                if t == '+':
                    stack.append(t1+t2)
                elif t == '-':
                    stack.append(t1-t2)
                elif t == '*':
                    stack.append(t1*t2)
                else:
                    stack.append(int(t1/t2))

        return stack[-1]


        