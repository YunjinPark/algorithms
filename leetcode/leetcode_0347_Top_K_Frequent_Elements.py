from collections import Counter


class Solution:
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        """
        time:O(NlogN), space:O(N)
        """
        c = Counter(nums)
        sorted_c = sorted(c.items(), key=lambda kv: kv[1], reverse=True)
        return [sorted_c[i][0] for i in range(k)]

    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        """
        time:O(NlogK) space:O(N)
        """
        c = Counter(nums)
        return heapq.nlargest(k, c.keys(), key=c.get)

    def topKFrequent_3(self, nums: List[int], k: int) -> List[int]:
        """
        time:O(N) space:O(N)
        """
        c = Counter(nums)
        a = [[] for i in range(len(nums))]
        for num, freq in c.items():
            a[-freq].append(num)
        return list(itertools.chain(*a))[:k]