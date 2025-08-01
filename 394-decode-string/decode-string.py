class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:
            if ch ==']':

                substr = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                     k = stack.pop() + k

                stack.append(substr * int(k))
                
            else:
                stack.append(ch)

        return ''.join(stack)
        