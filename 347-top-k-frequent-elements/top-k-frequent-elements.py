class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       c = Counter(nums)
       arr = c.most_common(k)

       return [a[0] for a in arr]