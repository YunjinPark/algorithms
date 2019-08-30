class Solution:
    #Gauss' Formula [Accepted]
    #time: O(1) space: O(1)
    def missingNumber1(self, nums: List[int]) -> int:
        return (len(nums) + 1) * len(nums) // 2 - sum(nums)
    #Bit Manipulation
    #time: O(1) space: O(1)
    def missingNumber2(self, nums: List[int]) -> int:
        res = len(nums)
        for i, n in enumerate(nums):
            res = res^i^n
        return res