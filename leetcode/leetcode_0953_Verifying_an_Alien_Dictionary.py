class Solution:
    def isAlienSorted_1(self, words: List[str], order: str) -> bool:
        """
        time: O(N) , space:O(N)
        """
        dic = {s: i for i, s in enumerate(order)}

        def f(s1, s2):
            for i in range(min(len(s1), len(s2))):
                if dic[s1[i]] == dic[s2[i]]: continue
                return True if dic[s1[i]] < dic[s2[i]] else False
            return True if len(s1) <= len(s2) else False

        for i in range(1, len(words)):
            if not f(words[i - 1], words[i]): return False
        return True

    def isAlienSorted_2(self, words: List[str], order: str) -> bool:
        """
        time:O(NlogN) , space:O(N)
        """
        dic = {s: i for i, s in enumerate(order)}
        return words == sorted(words, key=lambda string: tuple(dic[i] for i in string))