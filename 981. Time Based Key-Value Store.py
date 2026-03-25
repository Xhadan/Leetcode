class TimeMap:

    def __init__(self):
        # Dictionary to store key -> list of [timestamp, value]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # Get the list associated with the key (empty list if not found)
        values = self.store.get(key, [])

        # Binary Search to find the largest timestamp <= given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                # This is a potential candidate, look for a later one
                res = values[mid][1]
                l = mid + 1
            else:
                # This timestamp is too late, look earlier
                r = mid - 1
        
        return res