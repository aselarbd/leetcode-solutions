class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}
        open_bracket = {'(', '{', '['}

        for c in s:
            if c in open_bracket:
                stack.append(c)
            else:
                if stack:
                    popped = stack.pop()
                    if popped != bracket_map[c]:
                        return False
                else:
                    return False
                
        return True if len(stack)==0 else False
        