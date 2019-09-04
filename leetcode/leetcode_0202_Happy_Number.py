class Solution:
    #time: - space: O(1)
    def isHappy(self, n: int) -> bool:
        d = {}
        while (True):
            n = self.ftn(n)
            if n == 1: return True
            if n in d: return False
            d[n] = 0

    def ftn(self, x):
        s = 0
        for i in range(len(str(x))):
            s += (x % 10) ** 2
            x //= 10
        return s
