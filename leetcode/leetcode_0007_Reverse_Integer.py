class Solution:
    #time: log_{10}^x, space: O(1)
    def reverse(self, x: int) -> int:
        absX = abs(x)
        lenX = len(str(abs(x)))
        sign = 1 if x >= 0 else -1
        result = 0
        for i in range(lenX):
            result += (absX % 10) * 10 ** (lenX - i - 1)
            absX = absX // 10
        result *= sign
        return result if result >= -2 ** (31) and result <= 2 ** (31) - 1 else 0