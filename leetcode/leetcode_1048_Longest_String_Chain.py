from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        time: O(N), space: O(N)
        """
        dic = defaultdict(lambda: defaultdict(int))

        for word in words:
            dic[len(word)][word] = 1

        key = sorted(dic.keys())
        res = 1

        for k in range(1, len(key)):
            for word in dic[key[k]]:
                s = [1]
                for i in range(1, len(word) + 1):
                    tmp = word[:i - 1] + word[i:]
                    if tmp in dic[key[k - 1]]:
                        s.append(dic[key[k - 1]][tmp] + 1)
                m = max(s)
                dic[key[k]][word] = m
                if res < m: res = m
        return res
