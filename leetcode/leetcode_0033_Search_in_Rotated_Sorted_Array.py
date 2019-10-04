class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        time: O(log(len(nums)))
        space: O(1)
        '''
        if not nums: return -1

        def bs(s, e, t):
            l, r = s, e
            m = (l + r) // 2
            while (l <= r):
                if nums[m] == t:
                    return m
                elif nums[m] < t:
                    l = m + 1
                elif nums[m] > t:
                    r = m - 1
                m = (l + r) // 2
            return -1

        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while (l < r):
            if nums[m] > nums[m + 1]:
                break;
            elif nums[m] > nums[-1]:
                l = m
            elif nums[m] < nums[-1]:
                r = m
            m = (l + r) // 2

        tmp = bs(0, m, target)
        if tmp != -1: return tmp
        return bs(m + 1, len(nums) - 1, target)