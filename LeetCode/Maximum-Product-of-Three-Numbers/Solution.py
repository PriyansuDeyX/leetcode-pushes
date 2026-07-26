1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        nums.sort()
4        #prothome array ta sort korlam
5        return max(
6            nums[-1] * nums[-2] * nums[-3],
7            nums[0] * nums[1] * nums[-1]
8        )