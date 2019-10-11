class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    '''
    time: O(4^n/n^(1/2))
    space:O(4^n/n^(1/2))
    '''
        res = []
        def f(s, left, right):
            if left == n and right == n:
                res.append(s)
            if left < n:
                f(s+['('], left+1, right)
            if right < left:
                f(s+[')'], left, right+1)
            return
        f([], 0, 0)
        return [''.join(s) for s in res]