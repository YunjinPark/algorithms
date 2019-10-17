class Solution:
    def spiralOrder_1(self, matrix: List[List[int]]) -> List[int]:
        '''
        time: O(N) where N is the total number of elements in the input matrix
        space: O(N)
        '''
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        res = []

        def f(k):
            i = k
            for j in range(k, n - k):
                res.append(matrix[i][j])
            j = n - k - 1
            for i in range(k + 1, m - k):
                res.append(matrix[i][j])
            i = m - k - 1
            for j in range(n - k - 2, k - 1, -1):
                res.append(matrix[i][j])
            j = k
            for i in range(m - k - 2, k, -1):
                res.append(matrix[i][j])

        tmp = min(m, n) // 2
        for t in range(tmp):
            f(t)

        i, j = tmp, tmp
        if (m <= n) and (m % 2 == 1):
            for j in range(tmp, n - tmp):
                res.append(matrix[i][j])
        if (m > n) and (n % 2 == 1):
            for i in range(tmp, m - tmp):
                res.append(matrix[i][j])

        return res

    def spiralOrder_2(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])