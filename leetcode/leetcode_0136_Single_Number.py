class Solution:
    #hash table
    #time: O(N) space:O(N)
    def singleNumber1(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                del d[i]
            else:
                d[i] = 0
        return list(d.keys())[0]
    #Bit Manipulation
    #time: O(N) space:O(1)
    def singleNumber2(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            i ^= n
        return i