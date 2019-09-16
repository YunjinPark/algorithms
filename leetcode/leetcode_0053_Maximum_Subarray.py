class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        time: O(n)
        space: O(1)
        """
        a, b = 0, nums[0]
        for n in nums:
            a = max(n + a, n)
            b = max(b, a)
        return b
