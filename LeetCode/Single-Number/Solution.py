1class Solution:
2    def singleNumber(self, nums: list[int]) -> int:
3        single = 0
4        for num in nums:
5            single ^= num
6        return single