class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack  = [] # [temp, idx]

        for i,t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                _ , stackI = stack.pop()
                res[stackI] = i - stackI

            stack.append((t,i))
        return res
        