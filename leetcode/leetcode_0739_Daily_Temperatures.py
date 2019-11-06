class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''time:O(N), space:O(N)'''
        stack, res = [], [0 for _ in range(len(T))]
        for i in range(len(T) - 1, -1, -1):
            while (stack and stack[-1][1] <= T[i]):
                stack.pop()
            if stack: res[i] = (stack[-1][0] - i)
            stack.append([i, T[i]])
        return res