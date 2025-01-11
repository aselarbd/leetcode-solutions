from collections import deque

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        nums = deque([-1])
        right_max = arr[-1]
        
        for i in range(len(arr)-2,-1,-1):           
            nums.appendleft(right_max)
            right_max = max(right_max, arr[i])

        return list(nums)

        