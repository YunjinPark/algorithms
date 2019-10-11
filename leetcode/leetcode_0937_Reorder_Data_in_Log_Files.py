class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        time: O(NlogN), N is the total content of logs.
        space: O(N)
        '''
        l1 = [log for log in logs if log[-1].isalpha()]
        l2 = [log for log in logs if log[-1].isdigit()]

        return sorted(l1, key=(lambda x: (x.split(' ')[1:], x.split(' ')[0]))) + l2