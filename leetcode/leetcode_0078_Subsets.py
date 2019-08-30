class Solution:
    #time: O(n*2^n) space: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a = 0b0
        n = 0b1 << len((nums))
        result = []
        while (a < n):
            r = []
            for i in range(len(nums)):
                tmp = (a >> i)%2
                if tmp: r.append(nums[i])
            result.append(r)
            a += 1
        return result