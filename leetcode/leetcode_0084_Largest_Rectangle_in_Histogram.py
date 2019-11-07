class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''time: O(N), space: O(N)'''
        h = len(heights)
        left, right = [-1 for _ in range(h)], [h for _ in range(h)]

        for i in range(1, h):
            p = i - 1
            while (p >= 0 and heights[p] >= heights[i]):
                p = left[p]
            left[i] = p

        for i in range(h - 2, -1, -1):
            p = i + 1
            while (p < h and heights[p] >= heights[i]):
                p = right[p]
            right[i] = p

        res = 0
        for i in range(h):
            res = max(res, heights[i] * (right[i] - left[i] - 1))

        return res