class Solution:
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        '''
        time: O(N)
        space: O(N)
        N represents the number of elements in the input array.
        '''
        n = len(nums)
        res1 = [1 for _ in range(n)]
        res2 = [1 for _ in range(n)]
        for i in range(1, n):
            res1[i] = res1[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            res2[j] = res2[j + 1] * nums[j + 1]

        return [a * b for a, b in zip(res1, res2)]

    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        '''
        time: O(N)
        space: O(1)
        '''
        n = len(nums)
        res = [1 for _ in range(n)]
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        tmp = 1
        for j in range(n - 1, -1, -1):
            res[j] = res[j] * tmp
            tmp *= nums[j]
        return res
