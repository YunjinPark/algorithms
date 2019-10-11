import copy


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        time: O(MN)
        space: O(MN)
        """
        if not board: return []
        board2 = copy.deepcopy(board)
        m, n = len(board), len(board[0])

        def f(a, b):
            if a >= 0 and a < m and b >= 0 and b < n:
                return board2[a][b]
            return 0

        for i in range(m):
            for j in range(n):
                c = sum([f(i - 1, j - 1), f(i - 1, j), f(i - 1, j + 1),
                         f(i, j - 1), f(i, j + 1),
                         f(i + 1, j - 1), f(i + 1, j), f(i + 1, j + 1)])
                if board2[i][j] == 1:
                    if c != 2 and c != 3:
                        board[i][j] = 0
                else:
                    if c == 3:
                        board[i][j] = 1