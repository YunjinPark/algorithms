class Solution:
    def climbStairs(self, n):
        """
        time: O(N)
        space: O(1)
        """
        if n == 1 : return 1
        elif n == 2 : return 2
        else:
            a, b = 1, 2
            for _ in range(3, n+1):
                c = a + b
                a, b = b, c
        return c