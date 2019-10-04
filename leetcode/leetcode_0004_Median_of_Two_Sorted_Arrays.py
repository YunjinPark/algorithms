class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        time: O(log(min(nums1, nums2))
        space: O(1)
        '''
        if len(nums1) <= len(nums2):
            len_x, len_y = len(nums1), len(nums2)
            x, y = nums1, nums2
        else:
            len_x, len_y = len(nums2), len(nums1)
            x, y = nums2, nums1

        x_st, x_end = 0, len_x
        while (x_st <= x_end):
            part_x = (x_st + x_end) // 2
            part_y = (len_x + len_y + 1) // 2 - part_x

            left_x = x[part_x - 1] if part_x != 0 else -float('inf')
            right_x = x[part_x] if part_x != len_x else float('inf')

            left_y = y[part_y - 1] if part_y != 0 else -float('inf')
            right_y = y[part_y] if part_y != len_y else float('inf')

            if max(left_x, left_y) <= min(right_x, right_y):
                if (len_x + len_y) % 2 == 1: return max(left_x, left_y)
                if (len_x + len_y) % 2 == 0: return (max(left_x, left_y) + min(right_x, right_y)) / 2
            if left_x > right_y: x_end = part_x - 1
            if left_y > right_x: x_st = part_x + 1

