class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:
            if ch ==']':

                temp_str = []
                temp_int = []

                while stack and stack[-1] != '[':
                    temp_str.append(stack.pop())
                stack.pop()

                while stack and stack[-1].isdigit():
                     temp_int.append(stack.pop())

                count = int(''.join(temp_int[::-1]))

                for t in temp_str[::-1]*count:
                    stack.append(t)

            else:
                stack.append(ch)

        return ''.join(stack)
        