class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        def check_condition(ch1, ch2):
            if ch1.isupper() and ch2.islower() and (ch1.lower() == ch2) :
                return True
            if ch2.isupper() and ch1.islower() and (ch2.lower() == ch1) :
                return True
            return False

        for c in s:

            while stack and check_condition(stack[-1],c):
                stack.pop()
                c = -1
                break

            if c !=-1:
                stack.append(c)
            
        return ''.join(stack)
        