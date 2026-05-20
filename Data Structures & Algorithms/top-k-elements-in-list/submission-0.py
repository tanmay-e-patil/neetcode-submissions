class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        heap = []
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        for key,v in num_count.items():
            heapq.heappush(heap, [-v, key])
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
              
        