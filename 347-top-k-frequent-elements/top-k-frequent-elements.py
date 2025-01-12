class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        count_tuple = [ c for c in counter.items()]

        count_tuple.sort(key=lambda x: x[1], reverse=True)

        res = [ c[0] for c in count_tuple[:k]]

        return res
        