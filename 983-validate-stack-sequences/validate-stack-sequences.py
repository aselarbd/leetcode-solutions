class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = [pushed.pop(0)]

        for po in popped:

            while (stack and po != stack[-1]) and pushed:
                stack.append(pushed.pop(0))
            
            if stack and po == stack[-1]:
                stack.pop()
            
            if len(stack) ==0 and len(pushed)>0:
                stack.append(pushed.pop(0))

        
        return False if stack else True