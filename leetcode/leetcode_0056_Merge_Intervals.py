class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        time: O(n log n) , n: len(intervals)
        space: O(n)
        '''
        if len(intervals) <= 1: return intervals
        s_inter = sorted(intervals, key=lambda s: s[0])
        r = [s_inter[0]]
        for i in range(1, len(intervals)):
            if r[-1][1] >= s_inter[i][0] and r[-1][1] < s_inter[i][1]:
                r[-1] = [r[-1][0], s_inter[i][1]]
            elif r[-1][1] < s_inter[i][0]:
                r.append(s_inter[i])
        return r
