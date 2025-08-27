import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [-n for n in nums]
        heapq.heapify(res)
        
        for _ in range(k-1):
            heapq.heappop(res)
        
        return -res[0]
        