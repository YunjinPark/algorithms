class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dic = {i + 1: 0 for i in range(N)}

        for t in trust:
            dic.pop(t[0], None)
            if t[1] in dic: dic[t[1]] += 1

        tmp, res = 0, -1
        print(dic)
        for key in dic.keys():
            if dic[key] == N - 1:
                tmp += 1
                res = key
            if tmp > 2: return -1

        return res