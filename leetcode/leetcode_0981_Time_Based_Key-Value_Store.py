from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        time: O(1)
        """
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """
        time: O(logN), N is the number of entries in the TimeMap.
        """
        if len(self.d[key]) == 0: return ""

        l, r = 0, len(self.d[key]) - 1

        while (l <= r):
            m = (l + r) // 2
            tmp = self.d[key][m + 1][0] if m + 1 <= len(self.d[key]) - 1 else float('inf')
            if self.d[key][m][0] <= timestamp and tmp > timestamp:
                return self.d[key][m][1]
            elif self.d[key][m][0] < timestamp:
                l = m + 1
            elif self.d[key][m][0] > timestamp:
                r = m - 1
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)