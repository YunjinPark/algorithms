from collections import defaultdict, Counter

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ''' best time: O(N^2) worst time: O(N^4)
        space:O(N^2) '''
        n = len(nums)
        d = defaultdict(set)
        res = set()
        coun = Counter(nums)

        def f(list_4): # 해당 4개 조합이 원래 nums에서 나올 수 있는지 체크
            coun_4 = Counter(list_4)
            for i in coun_4:
                if coun_4[i] > coun[i]:
                    return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                for n_2 in d[target - s]:
                    if f(list(n_2) + [nums[i], nums[j]]): res.add(tuple(sorted(list(n_2) + [nums[i], nums[j]])))
                d[s].add(tuple(sorted([nums[i], nums[j]])))
        return res
