class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        heap = []
        for key,v in d.items():
            heapq.heappush(heap, [v,key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for v,key in heap]
