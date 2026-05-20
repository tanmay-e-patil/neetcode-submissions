class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #[-4, -1, -1, 0, 1, 2]
        # -1, -1, 2
        n = len(nums)
        res = []
        nums.sort()
        for k in range(n):
            if nums[k] > 0:
                break
            l = k + 1
            r = n - 1

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            while l < r: 
                threeSum = nums[l] + nums[r] + nums[k]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
