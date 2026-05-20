class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        res_list = []
        for interval in intervals:
            if not res_list:
                res_list.append(interval)
            elif res_list[-1][1] > interval[0]:
                res += 1
                res_list[-1][1] = min(res_list[-1][1], interval[1])
            else:
                res_list.append(interval)
        return res

            

        