from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        L,R = 0,len(nums)-1
        result = deque([])

        while L <= R:

            left_val = nums[L]**2
            right_val = nums[R]**2
            
            if left_val > right_val:
                result.appendleft(left_val)
                L += 1
            elif right_val > left_val:
                result.appendleft(right_val)
                R -= 1
            else:
                if L == R:
                    result.appendleft(right_val)
                else:
                    result.appendleft(right_val)
                    result.appendleft(left_val)

                L += 1    
                R -= 1

        return list(result)


        