"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda x: x.start)
        
        # res = defaultdict(list)
        days = 1
        # visited = {}
        # idx = 0
        groups = []
        for interval in intervals:
            if not groups:
                groups.append(interval.end)
                continue
            # is_nonoverlap = False
            found_spot = False
            for idx,end in enumerate(groups):
                if end <= interval.start:
                    groups[idx] = interval.end
                    found_spot = True
                    break
            if not found_spot:
                groups.append(interval.end)
                days += 1
        return days
        
                    

            
        # while len(visited) != len(intervals):
        #     if not visited:
        #         visited.add(intervals[])
        # for interval in intervals:
        #     if not res[day]:
        #         res[day].append(interval)
        #     elif res[day][-1].end > interval.start:
        #         day += 1
        #         res[day].append(interval)
        #     else:
        #         res[day].append(interval)
        # return day
        