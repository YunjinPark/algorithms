class Solution:
    def letterCombinations_1(self, digits: str) -> List[str]:
        """ time: O((3^N)*(4*M)) / space: O((3^N)*(4*M))
        N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8)
        and M is the number of digits in the input that maps to 4 letters (e.g. 7, 9),
        and N+M is the total number digits in the input."""
        mapping = {2: ['a', 'b', 'c'],
                   3: ['d', 'e', 'f'],
                   4: ['g', 'h', 'i'],
                   5: ['j', 'k', 'l'],
                   6: ['m', 'n', 'o'],
                   7: ['p', 'q', 'r', 's'],
                   8: ['t', 'u', 'v'],
                   9: ['w', 'x', 'y', 'z']
                   }

        def f(st, d):
            if not d: return res.append(st)
            for i in mapping[int(d[0])]:
                f(st + [i], d[1:])

        res = []
        f([], digits)

        return [''.join(r) for r in res] if len(digits) > 0 else []

    def letterCombinations_2(self, digits: str) -> List[str]:
        """ time: O((3^N)*(4*M)) / space: O((3^N)*(4*M))"""
        mapping = {2: ['a', 'b', 'c'],
                   3: ['d', 'e', 'f'],
                   4: ['g', 'h', 'i'],
                   5: ['j', 'k', 'l'],
                   6: ['m', 'n', 'o'],
                   7: ['p', 'q', 'r', 's'],
                   8: ['t', 'u', 'v'],
                   9: ['w', 'x', 'y', 'z']
                   }
        if len(digits) == 0: return []
        res = [[m] for m in mapping[int(digits[0])]]
        for d in digits[1:]:
            res = [r + [m] for m in mapping[int(d)] for r in res]

        return [''.join(r) for r in res]
