class Solution:
    def rob(self, nums: List[int]) -> int:
        '''time:O(N), space:O(N)'''
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        amount = copy.deepcopy(nums)
        amount[2] = max(nums[0] + nums[2], nums[1])

        for i in range(3, len(nums)):
            amount[i] = max(amount[i] + amount[i - 3], amount[i] + amount[i - 2], amount[i - 1])

        return max(amount[-1], amount[-2])