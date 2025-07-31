class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in bracket_map.values():  # Opening brackets
                stack.append(c)
            elif c in bracket_map:  # Closing brackets
                if not stack or stack.pop() != bracket_map[c]:
                    return False
            else:
                # Optional: handle unexpected characters
                return False

        return not stack
            