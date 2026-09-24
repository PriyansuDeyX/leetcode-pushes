1class Solution:
2    def smallestIndex(self, nums: list[int]) -> int:
3        for i in range(len(nums)):
4            digit_sum = sum(int(digit) for digit in str(nums[i]))
5            if digit_sum == i:
6                return i
7        return -1