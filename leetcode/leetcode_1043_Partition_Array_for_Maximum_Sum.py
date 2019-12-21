class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [A[0]]
        for i in range(1, len(A)):
            dp.append(max([(dp[i - j] if i - j >= 0 else 0) + max(A[i - j + 1:i + 1]) * j \
                           for j in range(1, min(K + 1, i + 2))]))
        return dp[-1]
