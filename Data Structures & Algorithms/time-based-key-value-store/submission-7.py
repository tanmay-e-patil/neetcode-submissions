class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = -1
        values = self.kv.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) //2
            if values[mid][1] <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        print(res, values)
        return values[res][0] if res != -1 else ""
        
