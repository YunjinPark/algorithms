class Solution:
    def numDecodings(self, s: str) -> int:
        """
        time: O(|s|)
        space: O(1)
        """
        if (not s) or int(s[0]) == 0: return 0
        if len(s) == 1: return 1

        if int(s[1]) == 0:
            if int(s[0]) > a= 3: return 0
            a, b = 0, 1
        elif int(s[:2]) > 26:
            a, b = 1, 1
        else:
            a, b = 1, 2

        c = b
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i - 1] not in ['1', '2']: return 0
                c, b = a, 0
            elif int(s[(i - 1):i + 1]) < 27:
                c = a + b
            else:
                c = b
            a, b = b, c
        return c