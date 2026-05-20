class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num_count = {}
        # heap = []
        # for num in nums:
        #     num_count[num] = num_count.get(num, 0) + 1
        # for key,v in num_count.items():
        #     heapq.heappush(heap, [-v, key])
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res
        num_count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        for n,c in num_count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for f in freq[i]:
                res.append(f)
                if len(res) == k:
                    return res
        return res


              
        