class Solution:
    #time: O(lon_{10}^{x}) space: O(1)
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        lenX = len(str(x))
        for i in range(lenX // 2):
            if (x // (10 ** (lenX - 1 - i))) % 10 != (x // (10 ** i)) % 10: return False
        return True

