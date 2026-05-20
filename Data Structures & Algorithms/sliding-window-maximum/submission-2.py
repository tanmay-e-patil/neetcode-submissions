class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        
        # l = 0
        # for r in range(k, len(nums) + 1):
        #     res.append(max(nums[l:r]))
        #     l += 1
        # return res

        q = collections.deque()
        l, r = 0, 0
        output = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

        return output
            
        