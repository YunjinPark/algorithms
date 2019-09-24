class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        time: O(|s|^2)
        space: O(1)
        """
        a, b = 0, 0
        m = 0
        for i in range(1, len(s)-1):
            j = 1
            while (i-j >= 0 and i+j < len(s)):
                if s[i-j] != s[i+j]: break
                j += 1
            if m < 2*(j-1)+1:
                m = 2*(j-1)+1
                a, b = i-(j-1), i+(j-1)
        for i in range(1, len(s)):
            j = 1
            while (i-j>=0 and i+j-1<len(s)):
                if s[i-j] != s[i+j-1]: break
                j += 1
            if m < 2*(j-1):
                m = 2*(j-1)
                a, b = i-(j-1), i+(j-1)-1
        return s[a:b+1]