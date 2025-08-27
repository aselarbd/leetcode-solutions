import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -1*n)
        
        for _ in range(k-1):
            heapq.heappop(h)
        
        return heapq.heappop(h) * -1
        