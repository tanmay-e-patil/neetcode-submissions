class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # l = 0
        # r = l + 1
        # res = []
        # while len(res) != len(temperatures):
        #     if r == len(temperatures):
        #         res.append(0)
        #         l += 1
        #         r = l + 1
        #     elif temperatures[r] > temperatures[l]:
        #         res.append(r - l)
        #         l += 1
        #         r = l + 1
        #     else:
        #         r += 1
        # return res

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append([t,i])
        return res


        