class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertIdx = 0
        for interval in intervals:
            if interval[0] < newInterval[0]:
                insertIdx += 1
            # elif interval[1] >= newInternval[0]:
            #     interval[1] = max(newInternval[1], interval[1])
        intervals.insert(insertIdx, newInterval)

        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            elif res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res




        