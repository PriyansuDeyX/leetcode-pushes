1class Solution:
2
3  def missingNumber(self, nums: list[int]) -> int:
4    n = len(nums)
5    expected_sum = n * (n + 1) // 2
6    actual_sum = sum(nums)
7
8    return expected_sum - actual_sum